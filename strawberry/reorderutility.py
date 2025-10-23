# -*- coding: utf-8 -*-
from __future__ import annotations

import os
import sys
import json
import time
import shutil
import datetime as dt
import threading
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import hashlib

# Rich UI
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import (
    Progress,
    BarColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    MofNCompleteColumn,
    TaskProgressColumn,
    TransferSpeedColumn,
)
from rich.prompt import Prompt, Confirm
from rich import box

# prompt_toolkit — OS-wide Tab completion (root/drive + sottodir)
try:
    from prompt_toolkit import prompt as pt_prompt
    from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter, PathCompleter
    from prompt_toolkit.validation import Validator, ValidationError
    HAVE_PT = True
except Exception:
    HAVE_PT = False

# opzionale (Linux)
try:
    from creationdateutils import Date as CreationDate
except Exception:
    CreationDate = None

console = Console()

# ------------------------ Config ------------------------
BUF_SIZE = 8 * 1024 * 1024  # 8MB
MAX_WORKERS = max(4, min(32, (os.cpu_count() or 4) * 2))
HASH_ALGO = "blake2b"
HASH_DIGEST = 32
MANIFEST_NAME = ".reorder_manifest.jsonl"

# -------------------- Estensioni -> Categoria --------------------
CATEGORIES: Dict[str, Tuple[str, Tuple[str, ...]]] = {
    # Documenti e testi
    "docs": ("Document Files", (
        ".txt", ".text", ".log", ".md", ".markdown", ".rst", ".rtf", ".tex", ".adoc",
        ".doc", ".docx", ".docm", ".dot", ".dotx", ".dotm",
        ".ppt", ".pptx", ".pptm", ".pot", ".potx", ".potm",
        ".xls", ".xlsx", ".xlsm", ".xltx", ".xltm",
        ".odt", ".ods", ".odp", ".odg", ".odm", ".odb",
        ".pdf", ".djvu",
    )),
    # Dati/Serializzazioni
    "data": ("Data files", (
        ".csv", ".tsv", ".psv", ".json", ".jsonl", ".yaml", ".yml", ".xml", ".toml", ".ini", ".conf", ".cfg",
        ".parquet", ".arrow", ".feather", ".avro", ".orc", ".h5", ".hdf5", ".npy", ".npz", ".mat", ".sav", ".dta",
    )),
    # Immagini raster
    "photo": ("Image files", (
        ".png", ".jpeg", ".jpg", ".jfif", ".jpe", ".tif", ".tiff", ".bmp", ".gif", ".webp", ".apng", ".jxl",
        ".heic", ".heif", ".avif",
        ".cr2", ".cr3", ".nef", ".arw", ".orf", ".raf", ".sr2", ".rw2", ".pef", ".dng", ".raw",
        ".psd", ".xcf",
    )),
    # Immagini vettoriali e design
    "vector": ("Vector & Design files", (
        ".svg", ".ai", ".eps", ".pdf", ".cdr", ".indd", ".idml", ".afdesign", ".afphoto", ".sketch", ".fig", ".xd",
        ".icns", ".cur",
    )),
    # Audio
    "audio": ("Audio files", (
        ".mp3", ".m4a", ".aac", ".ogg", ".oga", ".opus", ".flac", ".alac", ".wav", ".aif", ".aiff", ".ape", ".mka", ".mid", ".midi", ".kar",
    )),
    # Video
    "video": ("Video files", (
        ".mp4", ".m4v", ".mov", ".webm", ".ogv", ".avi", ".mkv", ".wmv", ".flv", ".f4v", ".mpeg", ".mpg", ".m2ts", ".ts", ".3gp", ".3g2", ".vob", ".rm", ".rmvb",
    )),
    # Sottotitoli
    "subtitles": ("Subtitle files", (
        ".srt", ".ass", ".ssa", ".vtt", ".sub", ".idx",
    )),
    # Font
    "font": ("Font files", (
        ".ttf", ".otf", ".woff", ".woff2", ".eot", ".suit", ".ttc",
    )),
    # Sorgenti / codice
    "source": ("Source Code files", (
        ".c", ".h", ".cpp", ".hpp", ".cc", ".hh", ".m", ".mm",
        ".cs", ".vb", ".java", ".kt", ".kts", ".scala", ".go", ".rs", ".swift",
        ".py", ".pyw", ".r", ".jl", ".pl", ".pm", ".rb", ".php", ".hs", ".lua", ".tcl", ".dart",
        ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".vue", ".svelte",
        ".sh", ".bash", ".zsh", ".ps1", ".psm1",
        ".sql", ".yaml", ".yml", ".toml", ".xml", ".xaml", ".json",
        ".sln", ".csproj", ".vbproj", ".fsproj", ".vcxproj", ".cmake", ".gradle", ".pom", ".iml",
        ".dockerfile", ".make", ".mk",
    )),
    # Script/Batch/Executable
    "executables": ("Executable files", (
        ".exe", ".com", ".bat", ".cmd", ".msi", ".msix", ".msixbundle", ".appx",
        ".apk", ".aab", ".ipa", ".xap",
    )),
    # Librerie
    "libraries": ("Library files", (
        ".dll", ".so", ".dylib", ".lib", ".a",
    )),
    # Archivi/compressi
    "compressed": ("Compressed files", (
        ".zip", ".rar", ".7z", ".tar", ".gz", ".tgz", ".bz", ".bz2", ".tbz", ".tbz2", ".xz", ".txz", ".zst", ".lz", ".lz4", ".cab", ".cpio", ".arj", ".lzh",
    )),
    # Pacchetti/installer
    "packages": ("Packages", (
        ".deb", ".rpm", ".snap", ".pkg", ".dnf", ".appimage", ".whl", ".egg", ".war", ".ear", ".msu",
    )),
    # Icone
    "icon": ("Icon files", (
        ".ico", ".icns", ".cur",
    )),
    # Jar
    "jar": ("Jar files", (".jar",)),
    # Immagini disco / virtualizzazione
    "diskimage": ("Disk Image files", (
        ".iso", ".img", ".bin", ".cue", ".dmg", ".vmdk", ".vdi", ".vhd", ".vhdx", ".qcow", ".qcow2", ".ovf", ".ova",
    )),
    # 3D/CAD
    "3d": ("3D model files", (
        ".blend", ".obj", ".fbx", ".3ds", ".stl", ".ply", ".dae", ".glb", ".gltf", ".step", ".stp", ".iges", ".igs", ".skp", ".sldprt", ".sldasm", ".dxf", ".dwg",
    )),
    # GIS/Geo
    "gis": ("GIS files", (
        ".shp", ".shx", ".dbf", ".prj", ".geojson", ".topojson", ".kml", ".kmz", ".gpx", ".mbtiles", ".tif", ".tiff",
    )),
    # E-book
    "ebooks": ("Ebook files", (
        ".epub", ".mobi", ".azw", ".azw3", ".fb2",
    )),
    # Email/archivi posta
    "mail": ("Email files", (
        ".eml", ".msg", ".pst", ".ost", ".mbox",
    )),
    # Database
    "database": ("Database files", (
        ".sql", ".sqlite", ".db", ".db3", ".sqlite3", ".mdb", ".accdb", ".mdf", ".ldf",
    )),
    # Notebook / report
    "notebooks": ("Notebook files", (
        ".ipynb", ".rmd", ".qmd",
    )),
    # Certificati/chiavi
    "certs": ("Certificates & Keys", (
        ".pem", ".crt", ".cer", ".der", ".p7b", ".pfx", ".p12", ".key", ".jks",
    )),
    # Torrent/log
    "torrent": ("Torrents", (".torrent",)),
    "logs": ("Logs", (".log", ".har")),
}

EXT_TO_CATEGORY: Dict[str, str] = {}
for _, (folder, exts) in CATEGORIES.items():
    for ext in exts:
        EXT_TO_CATEGORY[ext.lower()] = folder

# ------------------------ Prompt OS-wide ------------------------
def _windows_drives() -> List[str]:
    if os.name != "nt":
        return []
    import string
    return [f"{l}:\\"
            for l in string.ascii_uppercase
            if os.path.exists(f"{l}:\\")]

class DirValidator(Validator):
    def validate(self, document):
        t = document.text.strip()
        if not t:
            return
        p = Path(os.path.expanduser(t))
        if not (p.exists() and p.is_dir()):
            raise ValidationError(message="Directory non valida", cursor_position=len(document.text))

if HAVE_PT:
    class OSPathCompleter(Completer):
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

def ask_directory(label: str, default: Optional[str] = None) -> str:
    default = default or str(Path.cwd())
    if HAVE_PT:
        completer = FuzzyCompleter(OSPathCompleter())
        try:
            ans = pt_prompt(
                f"{label} [{default}]: ",
                completer=completer,
                complete_while_typing=True,
                validator=DirValidator(),
                validate_while_typing=False,
            ).strip()
        except Exception:
            ans = ""
        ans = ans or default
        return str(Path(os.path.expanduser(ans)))
    return Prompt.ask(label, default=default)

# ------------------------ Utilità core ------------------------
_manifest_lock = threading.Lock()

def _hash_file(path: Path) -> str:
    h = hashlib.blake2b(digest_size=HASH_DIGEST)
    with path.open("rb", buffering=0) as f:
        while True:
            b = f.read(BUF_SIZE)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def _same_device(src: Path, dst_dir: Path) -> bool:
    try:
        return src.stat().st_dev == dst_dir.stat().st_dev
    except FileNotFoundError:
        parent = dst_dir
        while not parent.exists():
            parent = parent.parent
        return src.stat().st_dev == parent.stat().st_dev

def _unique_destination(dst_dir: Path, name: str) -> Path:
    dst = dst_dir / name
    if not dst.exists():
        return dst
    ts = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    stem, suffix = os.path.splitext(name)
    cand = dst_dir / f"{ts}[dx]_{stem}{suffix}"
    i = 1
    while cand.exists():
        cand = dst_dir / f"{ts}[dx]_{stem}_{i}{suffix}"
        i += 1
    return cand

def _write_manifest(manifest_path: Path, record: dict) -> None:
    line = json.dumps(record, ensure_ascii=False)
    with _manifest_lock:
        with manifest_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

def _safe_move(src: Path, dst_dir: Path, manifest_path: Path) -> Tuple[bool, str, Path, Path, int]:
    """Rinomina su stesso device; altrimenti copia con verifica hash e poi elimina sorgente."""
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        dst = _unique_destination(dst_dir, src.name)
        src_size = src.stat().st_size

        if _same_device(src, dst_dir):
            os.replace(src, dst)
            rec = {"op": "move", "src": str(src), "dst": str(dst), "size": src_size, "hash": None, "ts": time.time()}
            _write_manifest(manifest_path, rec)
            return True, "moved", src, dst, src_size
        else:
            h_src = hashlib.blake2b(digest_size=HASH_DIGEST)
            with src.open("rb", buffering=0) as fsrc, dst.open("wb", buffering=0) as fdst:
                while True:
                    chunk = fsrc.read(BUF_SIZE)
                    if not chunk:
                        break
                    h_src.update(chunk)
                    fdst.write(chunk)
                fdst.flush()
                os.fsync(fdst.fileno())

            h_dst = _hash_file(dst)
            ok = (h_src.hexdigest() == h_dst)
            if ok:
                src.unlink()
                rec = {"op": "copy-verify-delete", "src": str(src), "dst": str(dst), "size": src_size, "hash": h_dst, "ts": time.time()}
                _write_manifest(manifest_path, rec)
                return True, "copied+verified", src, dst, src_size
            else:
                rec = {
                    "op": "copy-verify-failed",
                    "src": str(src),
                    "dst": str(dst),
                    "size": src_size,
                    "hash_src": h_src.hexdigest(),
                    "hash_dst": h_dst,
                    "ts": time.time(),
                }
                _write_manifest(manifest_path, rec)
                return False, "verify_failed", src, dst, src_size
    except Exception as e:
        return False, f"error: {e}", src, dst if "dst" in locals() else dst_dir, 0

def _iter_files(base: Path, recursive: bool) -> Iterable[Path]:
    if recursive:
        for root, _dirs, files in os.walk(base):
            r = Path(root)
            for name in files:
                yield r / name
    else:
        with os.scandir(base) as it:
            for e in it:
                if e.is_file():
                    yield Path(e.path)

def _category_for(path: Path) -> Optional[str]:
    return EXT_TO_CATEGORY.get(path.suffix.lower())

def _banner(title: str):
    console.print(Panel.fit(f"[bold magenta]{title}[/bold magenta]", border_style="magenta"))

def _summary_table(moved: int, failed: int) -> Table:
    t = Table(title="Summary", box=box.SIMPLE_HEAVY)
    t.add_column("Moved", justify="right", style="green")
    t.add_column("Failed", justify="right", style="red")
    t.add_row(str(moved), str(failed))
    return t

def _guess_copy_workers() -> int:
    env = os.getenv("REORDER_IO_CONCURRENCY")
    if env:
        try:
            return max(1, min(32, int(env)))
        except ValueError:
            pass
    cpu = os.cpu_count() or 4
    # Conservativo per I/O: pochi worker per non saturare il disco
    return min(8, max(2, cpu // 2))

def _execute_balanced(pairs: List[Tuple[Path, Path]], manifest_path: Path, title_prefix: str = "Reorder") -> Tuple[int, int]:
    """Bilancia rename (stesso device) e copy+verify (device diverso), ordinando i copy per dimensione."""
    moves: List[Tuple[Path, Path]] = []
    copies: List[Tuple[Path, Path, int]] = []

    for src, dst in pairs:
        if _same_device(src, dst):
            moves.append((src, dst))
        else:
            try:
                size = src.stat().st_size
            except Exception:
                size = 0
            copies.append((src, dst, size))

    # Ordina le copie per dimensione decrescente per ridurre lo "straggling".
    copies.sort(key=lambda x: x[2], reverse=True)
    total_bytes = sum(size for _, _, size in copies)

    moved = failed = 0
    move_workers = min(MAX_WORKERS, max(4, len(moves))) if moves else 0
    copy_workers = _guess_copy_workers() if copies else 0

    prog_cols = (
        "{task.description}",
        BarColumn(),
        TaskProgressColumn(),
        MofNCompleteColumn(),
        TransferSpeedColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
    )

    with Progress(*prog_cols, console=console) as progress:
        # Task per rename (conteggio file) e copia (byte)
        task_moves = progress.add_task(f"{title_prefix} — Renaming", total=len(moves)) if moves else None
        task_copy  = progress.add_task(f"{title_prefix} — Copying", total=total_bytes) if copies else None

        # Esecutori separati per non far contendere I/O con tante rename veloci
        futures = []

        if moves:
            move_fn = partial(_safe_move, manifest_path=manifest_path)
            with ThreadPoolExecutor(max_workers=move_workers) as exm:
                for src, dst in moves:
                    futures.append(("move", exm.submit(move_fn, src, dst)))
                for kind, fut in [(k, f) for (k, f) in futures if k == "move"]:
                    ok, msg, src, dst, size = fut.result()
                    moved += int(ok)
                    failed += int(not ok)
                    if not ok:
                        console.print(f"[red]Failed[/red] {src} -> {dst} ({msg})")
                    if task_moves is not None:
                        progress.advance(task_moves, 1)

        if copies:
            futures = []
            copy_fn = partial(_safe_move, manifest_path=manifest_path)
            with ThreadPoolExecutor(max_workers=copy_workers) as exc:
                for src, dst, size in copies:
                    futures.append(exc.submit(copy_fn, src, dst))
                for fut in as_completed(futures):
                    ok, msg, src, dst, size = fut.result()
                    moved += int(ok)
                    failed += int(not ok)
                    if not ok:
                        console.print(f"[red]Failed[/red] {src} -> {dst} ({msg})")
                    if task_copy is not None and size:
                        progress.advance(task_copy, size)

    return moved, failed

# ------------------------------------------------------ eR ------------------------------------------------------
def eR(p, recursive):
    _banner("Reorder by extension")
    if p == "":
        p = ask_directory("Enter a directory", str(Path.cwd()))
    base = Path(p).expanduser().resolve()
    if not base.exists() or not base.is_dir():
        console.print("[bold red]Invalid directory[/bold red]")
        return

    console.print(f"SELECTED DIRECTORY: [cyan]{base}[/cyan]")

    dest_map: Dict[str, Path] = {folder: base / folder for folder, _ in CATEGORIES.values()}
    manifest_path = base / MANIFEST_NAME

    pairs: List[Tuple[Path, Path]] = []
    for path in _iter_files(base, recursive=recursive):
        cat = _category_for(path)
        if not cat:
            continue
        dst_dir = dest_map[cat]
        if dst_dir in path.parents:
            continue
        pairs.append((path, dst_dir))

    if not pairs:
        console.print("[yellow]Any file with recognized extension has been found[/yellow]")
        return

    moved, failed = _execute_balanced(pairs, manifest_path, title_prefix="By Extension")
    console.print(_summary_table(moved, failed))

# ------------------------------------------------------ aR ------------------------------------------------------
def aR(dy, e, n):
    _banner("Advanced Reorder")
    if dy == "":
        dy = ask_directory("Enter a directory", str(Path.cwd()))
        console.print(f"SELECTED DIRECTORY: [{dy}]")
    base = Path(dy).expanduser().resolve()

    if e == "":
        e = Prompt.ask("Enter an extension (e.g. .pdf)")
    if not e.startswith("."):
        console.print("[bold red]E: you haven't inserted an extension![/bold red]")
        aR("", "", "")
        return
    if n == "":
        n = Prompt.ask("Enter the name of the new folder where the files will go")

    dst_dir = base / n
    manifest_path = base / MANIFEST_NAME

    pairs: List[Tuple[Path, Path]] = []
    with os.scandir(base) as it:
        for entry in it:
            if entry.is_file() and entry.name.lower().endswith(e.lower()):
                pairs.append((Path(entry.path), dst_dir))

    if not pairs:
        console.print("[yellow]No files found[/yellow]")
        return

    moved, failed = _execute_balanced(pairs, manifest_path, title_prefix=f"Advanced ({e})")
    console.print(_summary_table(moved, failed))

# ------------------------------------------------------ kwR ------------------------------------------------------
def kwR(dy, kw, n):
    _banner("Reorder by keyword")
    if dy == "":
        dy = ask_directory("Enter a directory", str(Path.cwd()))
        console.print(f"SELECTED DIRECTORY: [{dy}]")
    base = Path(dy).expanduser().resolve()

    if kw == "":
        kw = Prompt.ask("Enter a keyword")
    if n == "":
        n = Prompt.ask("Enter a name for the folder where the files will go")

    dst_dir = base / n
    manifest_path = base / MANIFEST_NAME

    pairs: List[Tuple[Path, Path]] = []
    with os.scandir(base) as it:
        for entry in it:
            if entry.is_file() and kw in entry.name:
                pairs.append((Path(entry.path), dst_dir))

    if not pairs:
        console.print("[yellow]No files found[/yellow]")
        return

    moved, failed = _execute_balanced(pairs, manifest_path, title_prefix=f"Keyword <{kw}>")
    console.print(_summary_table(moved, failed))

# ------------------------------------------------------ LbdR (Linux) ------------------------------------------------------
def LbdR(dy, dR1, dR2, e):
    _banner("Reorder by Date (Linux)")
    if sys.platform != "linux":
        console.print("[yellow]Use bdR on non-Linux systems[/yellow]")
        return

    if dy == "":
        dy = ask_directory("Enter a directory", str(Path.cwd()))
        console.print(f"SELECTED DIRECTORY: [{dy}]")
    base = Path(dy).expanduser().resolve()

    if dR1 == "" and dR2 == "" and e == "":
        dR1 = Prompt.ask("Enter the first date (YYYY-mm-dd)")
        dR2 = Prompt.ask("Enter the second date (YYYY-mm-dd)")
    d1 = dt.datetime.strptime(dR1, "%Y-%m-%d")
    d2 = dt.datetime.strptime(dR2, "%Y-%m-%d")

    ext_filter = e
    if e == "":
        if Confirm.ask("Do you want to specify an extension?"):
            ext_filter = Prompt.ask("Insert an extension (e.g. .pdf)")
            if not ext_filter.startswith("."):
                console.print("[bold red]E: You haven't inserted an extension![/bold red]")
                LbdR("", "", "", "")
                return
        else:
            ext_filter = ""

    dst_dir = base / f"Files from {d1:%d} {d1:%B} {d1:%Y} to {d2:%d} {d2:%B} {d2:%Y}" + (f" ({ext_filter})" if ext_filter else "")
    manifest_path = base / MANIFEST_NAME

    pairs: List[Tuple[Path, Path]] = []
    with os.scandir(base) as it:
        for entry in it:
            if not entry.is_file():
                continue
            try:
                if CreationDate is not None:
                    created_str = CreationDate.getDateFromFile(entry.path)
                    created = dt.datetime.strptime(created_str, "%a %b %d %H:%M:%S %Y")
                else:
                    created = dt.datetime.fromtimestamp(os.path.getmtime(entry.path))
            except Exception:
                created = dt.datetime.fromtimestamp(os.path.getmtime(entry.path))

            if d1 <= created <= d2 and (not ext_filter or entry.name.lower().endswith(ext_filter.lower())):
                pairs.append((Path(entry.path), dst_dir))

    if not pairs:
        console.print("[yellow]No files found[/yellow]")
        return

    moved, failed = _execute_balanced(pairs, manifest_path, title_prefix="By Date (Linux)")
    console.print(_summary_table(moved, failed))

# ------------------------------------------------------ bdR (non-Linux) ------------------------------------------------------
def bdR(dy, dR1, dR2, e):
    if sys.platform == "linux":
        console.print("[yellow]GNU/Linux doesn't support birthtime; use LbdR[/yellow]")
        return

    _banner("Reorder by Date")
    if dy == "":
        dy = ask_directory("Enter a directory", str(Path.cwd()))
        console.print(f"SELECTED DIRECTORY: [{dy}]")
    base = Path(dy).expanduser().resolve()

    if dR1 == "" and dR2 == "" and e == "":
        dR1 = Prompt.ask("Enter the first date (YYYY-mm-dd)")
        dR2 = Prompt.ask("Enter the second date (YYYY-mm-dd)")
    d1 = dt.datetime.strptime(dR1, "%Y-%m-%d")
    d2 = dt.datetime.strptime(dR2, "%Y-%m-%d")

    ext_filter = e
    if e == "":
        if Confirm.ask("Do you want to specify an extension?"):
            ext_filter = Prompt.ask("Insert an extension (e.g. .pdf)")
            if not ext_filter.startswith("."):
                console.print("[bold red]E: You haven't inserted an extension![/bold red]")
                bdR("", "", "", "")
                return
        else:
            ext_filter = ""

    dst_dir = base / f"Files from {d1:%d} {d1:%B} {d1:%Y} to {d2:%d} {d2:%B} {d2:%Y}" + (f" ({ext_filter})" if ext_filter else "")
    manifest_path = base / MANIFEST_NAME

    pairs: List[Tuple[Path, Path]] = []
    with os.scandir(base) as it:
        for entry in it:
            if not entry.is_file():
                continue
            try:
                birth = dt.datetime.fromtimestamp(os.stat(entry.path).st_birthtime)
            except Exception:
                birth = dt.datetime.fromtimestamp(os.path.getmtime(entry.path))
            if d1 <= birth <= d2 and (not ext_filter or entry.name.lower().endswith(ext_filter.lower())):
                pairs.append((Path(entry.path), dst_dir))

    if not pairs:
        console.print("[yellow]No files found[/yellow]")
        return

    moved, failed = _execute_balanced(pairs, manifest_path, title_prefix="By Date")
    console.print(_summary_table(moved, failed))
