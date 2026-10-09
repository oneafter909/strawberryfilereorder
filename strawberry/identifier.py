# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
import json
import time
import stat
import hashlib
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Optional, DefaultDict
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed

# Rich (progress + output chiaro)
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import (
        Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn,
        MofNCompleteColumn, TaskProgressColumn, TransferSpeedColumn
    )
    from rich import box
    HAVE_RICH = True
    console = Console()
except Exception:
    HAVE_RICH = False
    class _Dummy:
        def print(self, *a, **k): print(*a)
    console = _Dummy()

# prompt_toolkit (tab-completion su tutto l’OS)
try:
    from prompt_toolkit import prompt as pt_prompt
    from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter, PathCompleter
    from prompt_toolkit.validation import Validator, ValidationError
    HAVE_PT = True
except Exception:
    HAVE_PT = False

BUF_SIZE = 8 * 1024 * 1024  # 8MB
HEAD_CHUNK = 256 * 1024     # 256KB per hash "parziale"
DIGEST_SIZE = 32            # 256-bit
MANIFEST_NAME = ".duplicate_manifest.jsonl"

# blake3 se disponibile (più veloce), fallback a blake2b
try:
    import blake3
    def _new_hasher():
        return blake3.blake3()
    def _hexdigest(h) -> str:
        return h.hexdigest(length=32)  # 256-bit
except Exception:
    def _new_hasher():
        return hashlib.blake2b(digest_size=DIGEST_SIZE)
    def _hexdigest(h) -> str:
        return h.hexdigest()

# ------------------------------- util -------------------------------
def _is_regular_file(p: Path) -> bool:
    try:
        st = p.lstat()
        return stat.S_ISREG(st.st_mode)
    except Exception:
        return False

def _iter_files(base: Path, recursive: bool) -> Iterable[Path]:
    if recursive:
        for root, dirs, files in os.walk(base):
            # opzionale: ignora dir nascosti; commenta se non serve
            # dirs[:] = [d for d in dirs if not d.startswith(".")]
            for name in files:
                yield Path(root) / name
    else:
        with os.scandir(base) as it:
            for e in it:
                if e.is_file(follow_symlinks=False):
                    yield Path(e.path)

def _hash_path(path: Path, first_bytes_only: Optional[int] = None) -> Tuple[str, int]:
    h = _new_hasher()
    size = 0
    with path.open("rb", buffering=0) as f:
        if first_bytes_only:
            # hash parziale
            to_read = first_bytes_only
            while to_read > 0:
                chunk = f.read(min(BUF_SIZE, to_read))
                if not chunk:
                    break
                h.update(chunk)
                to_read -= len(chunk)
            size = path.stat().st_size
        else:
            # hash completo stream
            while True:
                chunk = f.read(BUF_SIZE)
                if not chunk:
                    break
                h.update(chunk)
                size += len(chunk)
    return _hexdigest(h), size if size else path.stat().st_size

def _human(n: int) -> str:
    step = 1024.0
    for unit in ["B","KB","MB","GB","TB","PB"]:
        if n < step:
            return f"{n:.2f} {unit}"
        n /= step
    return f"{n:.2f} EB"

def _guess_workers(io_bound: bool = True) -> int:
    env = os.getenv("DUP_WORKERS")
    if env:
        try:
            v = int(env)
            if v > 0:
                return min(64, v)
        except ValueError:
            pass
    cpu = os.cpu_count() or 4
    if io_bound:
        # conservativo per non saturare il disco, ma sfrutta SSD
        return min(16, max(4, cpu))
    return max(1, cpu // 2 or 1)

def _banner(title: str):
    if HAVE_RICH:
        console.print(Panel.fit(f"[bold magenta]{title}[/bold magenta]", border_style="magenta"))
    else:
        console.print(f"== {title} ==")

# prompt directory con completion su tutto l’OS
def _windows_drives() -> List[str]:
    if os.name != "nt":
        return []
    import string
    return [f"{l}:\\"
            for l in string.ascii_uppercase
            if os.path.exists(f"{l}:\\")]

if HAVE_PT:
    class _DirValidator(Validator):
        def validate(self, document):
            t = document.text.strip()
            if not t:
                return
            p = Path(os.path.expanduser(t))
            if not (p.exists() and p.is_dir()):
                raise ValidationError(message="Directory non valida", cursor_position=len(document.text))

    class _OSPathCompleter(Completer):
        def __init__(self):
            self._pc = PathCompleter(expanduser=True, only_directories=True)

        def get_completions(self, document, complete_event):
            text = document.text_before_cursor.strip()
            if text == "":
                if os.name == "nt":
                    for d in _windows_drives():
                        yield Completion(d, start_position=0)
                else:
                    yield Completion("/", start_position=0)
                yield Completion(str(Path.home()) + os.sep, start_position=0, display="~"+os.sep)
            for c in self._pc.get_completions(document, complete_event):
                yield c

def _ask_directory(label: str, default: Optional[str] = None) -> str:
    default = default or str(Path.cwd())
    if HAVE_PT:
        comp = FuzzyCompleter(_OSPathCompleter())
        try:
            ans = pt_prompt(
                f"{label} [{default}]: ",
                completer=comp,
                complete_while_typing=True,
                validator=_DirValidator(),
                validate_while_typing=False,
            ).strip()
        except Exception:
            ans = ""
        return str(Path(os.path.expanduser(ans or default)))
    # fallback
    try:
        ans = input(f"{label} [{default}]: ").strip()
    except EOFError:
        ans = ""
    return str(Path(os.path.expanduser(ans or default)))

# -------------------------- core duplicate finder --------------------------
def _phase_group_by_size(paths: List[Path]) -> Dict[int, List[Path]]:
    groups: DefaultDict[int, List[Path]] = defaultdict(list)
    for p in paths:
        try:
            if not _is_regular_file(p):
                continue
            sz = p.stat().st_size
            if sz == 0:
                # i file vuoti sono tutti "duplicati" tra loro
                groups[0].append(p)
            else:
                groups[sz].append(p)
        except Exception:
            continue
    return groups

def _phase_head_hash(groups_by_size: Dict[int, List[Path]], workers: int) -> Dict[Tuple[int,str], List[Path]]:
    result: DefaultDict[Tuple[int,str], List[Path]] = defaultdict(list)
    tasks: List[Path] = []
    for sz, lst in groups_by_size.items():
        if len(lst) > 1 and sz > 0:
            tasks.extend(lst)
    if not tasks:
        return {}

    if HAVE_RICH:
        prog_cols = ("{task.description}", BarColumn(), TaskProgressColumn(), MofNCompleteColumn(), TimeElapsedColumn(), TimeRemainingColumn())
        progress = Progress(*prog_cols, transient=True, console=console)
    else:
        progress = None

    with (progress or _nullcontext()):
        task = progress.add_task("Head hash", total=len(tasks)) if progress else None
        out_lock = None  # non serve stampare per task
        def worker(p: Path):
            try:
                h, _ = _hash_path(p, first_bytes_only=min(HEAD_CHUNK, p.stat().st_size))
                return (p.stat().st_size, h, p)
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [ex.submit(worker, p) for p in tasks]
            for f in as_completed(futs):
                r = f.result()
                if r is None:
                    if progress and task is not None: progress.advance(task)
                    continue
                sz, hh, p = r
                result[(sz, hh)].append(p)
                if progress and task is not None: progress.advance(task)
    return result

def _phase_full_hash(groups_by_head: Dict[Tuple[int,str], List[Path]], workers: int) -> Dict[Tuple[int,str], List[Path]]:
    final: DefaultDict[Tuple[int,str], List[Path]] = defaultdict(list)
    tasks: List[Path] = []
    for _k, lst in groups_by_head.items():
        if len(lst) > 1:
            tasks.extend(lst)
    if not tasks:
        return {}

    # ordinamento per dimensione decrescente per ridurre lo straggling
    tasks.sort(key=lambda p: p.stat().st_size if p.exists() else 0, reverse=True)

    if HAVE_RICH:
        prog_cols = ("{task.description}", BarColumn(), TaskProgressColumn(), MofNCompleteColumn(), TransferSpeedColumn(), TimeElapsedColumn(), TimeRemainingColumn())
        progress = Progress(*prog_cols, transient=True, console=console)
    else:
        progress = None

    with (progress or _nullcontext()):
        task = progress.add_task("Full hash", total=len(tasks)) if progress else None

        def worker(p: Path):
            try:
                h, _ = _hash_path(p, first_bytes_only=None)
                return (p.stat().st_size, h, p)
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [ex.submit(worker, p) for p in tasks]
            for f in as_completed(futs):
                r = f.result()
                if r is None:
                    if progress and task is not None: progress.advance(task)
                    continue
                sz, fh, p = r
                final[(sz, fh)].append(p)
                if progress and task is not None: progress.advance(task)
    return final

class _nullcontext:
    def __enter__(self): return None
    def __exit__(self, *exc): return False

def _render_report(dups: Dict[Tuple[int,str], List[Path]], total_files: int, elapsed: float) -> None:
    groups = [(k, v) for k, v in dups.items() if len(v) > 1]
    groups.sort(key=lambda kv: kv[0][0], reverse=True)  # per dimensione
    dup_count = sum(len(v)-1 for _, v in groups)
    reclaim = sum((len(v)-1) * sz for (sz, _), v in groups)

    if HAVE_RICH:
        console.print(Panel.fit(f"[bold]File scansionati:[/bold] {total_files}  •  [bold]Gruppi duplicati:[/bold] {len(groups)}  •  [bold]Doppioni:[/bold] {dup_count}  •  [bold]Recuperabile:[/bold] {_human(reclaim)}  •  [bold]Tempo:[/bold] {elapsed:.2f}s", border_style="cyan"))
        t = Table(title="Duplicati", box=box.SIMPLE_HEAVY)
        t.add_column("Dimensione", justify="right")
        t.add_column("Hash", overflow="fold")
        t.add_column("Percorsi", overflow="fold")
        for (sz, h), paths in groups:
            t.add_row(_human(sz), h, "\n".join(str(p) for p in paths))
        console.print(t)
    else:
        console.print(f"Scansionati: {total_files} • Gruppi duplicati: {len(groups)} • Doppioni: {dup_count} • Recuperabile: {_human(reclaim)} • Tempo: {elapsed:.2f}s")
        for (sz, h), paths in groups:
            print(f"\n== {_human(sz)} | {h}")
            for p in paths:
                print(f"   - {p}")

def _write_manifest(base: Path, dups: Dict[Tuple[int,str], List[Path]], elapsed: float) -> Path:
    out = base / MANIFEST_NAME
    with out.open("a", encoding="utf-8") as f:
        for (sz, h), paths in dups.items():
            if len(paths) < 2:
                continue
            rec = {
                "op": "duplicate_group",
                "size": sz,
                "hash": h,
                "count": len(paths),
                "paths": [str(p) for p in paths],
                "ts": time.time(),
                "elapsed": elapsed,
                "algo": "blake3" if "blake3" in sys.modules else "blake2b-256",
                "head_chunk": HEAD_CHUNK
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return out

# --------------------------------- API ---------------------------------
def SearchDuplicate(dir: str, recursive: bool = False) -> None:
    """
    Cerca duplicati in modo preciso e veloce:
      1) raggruppa per dimensione
      2) hash parziale (256KB)
      3) hash completo sui candidati
    Log JSONL scritto in .duplicate_manifest.jsonl nella directory selezionata.
    """
    _banner("Duplicate Finder")

    if dir:
        base = Path(dir).expanduser().resolve()
    else:
        base = Path(_ask_directory("Inserisci un percorso", str(Path.cwd()))).expanduser().resolve()

    if not base.exists() or not base.is_dir():
        console.print("[red]Percorso non valido[/red]")
        return

    start = time.time()
    # 1) enumerazione
    paths = [p for p in _iter_files(base, recursive=recursive) if _is_regular_file(p)]
    total_files = len(paths)
    if total_files == 0:
        console.print("[yellow]Nessun file trovato[/yellow]")
        return

    # 2) raggruppa per dimensione
    by_size = _phase_group_by_size(paths)
    # filtra solo taglie con >1 file
    by_size = {sz: lst for sz, lst in by_size.items() if len(lst) > 1}

    if not by_size:
        elapsed = time.time() - start
        console.print(f"[green]Nessun duplicato trovato[/green] ({elapsed:.2f}s)")
        return

    io_workers = _guess_workers(io_bound=True)

    # 3) hash parziale
    by_head = _phase_head_hash(by_size, workers=io_workers)
    by_head = {k: v for k, v in by_head.items() if len(v) > 1}

    if not by_head:
        elapsed = time.time() - start
        console.print(f"[green]Nessun duplicato trovato[/green] ({elapsed:.2f}s)")
        return

    # 4) hash completo
    by_full = _phase_full_hash(by_head, workers=io_workers)
    dups = {k: v for k, v in by_full.items() if len(v) > 1}

    elapsed = time.time() - start

    if not dups:
        console.print(f"[green]Nessun duplicato trovato[/green] ({elapsed:.2f}s)")
        return

    _render_report(dups, total_files, elapsed)
    out = _write_manifest(base, dups, elapsed)
    if HAVE_RICH:
        console.print(f"[dim]Log: {out}[/dim]")
    else:
        print(f"Log: {out}")

# esecuzione diretta
if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    SearchDuplicate(arg, recursive=False)
