
default : bundle clean

bundle:
	# create bundle folder and copy package modules
	mkdir -p bundle
	cp strawberry/__main__.py bundle
	cp strawberry/GUI.py bundle
	cp strawberry/swb.py bundle
	cp strawberry/reorderutility.py bundle
	cp strawberry/creationdateutils.py bundle
	cp strawberry/identifier.py bundle
	rm -rf bundle/*.dist-info

	# Ensure a local .venv and install requirements (if not already present)
	if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
	fi
	. .venv/bin/activate && pip install --upgrade pip >/dev/null 2>&1 || true
	# install requirements into .venv (fast if already installed)
	. .venv/bin/activate && pip install -r requirements.txt >/dev/null 2>&1 || true

	# Vendor minimal dependencies (rich and a few of its deps) from the project's .venv
	cp -R .venv/lib/python*/site-packages/rich bundle/ 2>/dev/null || true
	cp -R .venv/lib/python*/site-packages/pygments bundle/ 2>/dev/null || true
	# copy markdown-it-py/markdown_it package (some installs use markdown_it, others markdown_it_py)
	cp -R .venv/lib/python*/site-packages/markdown_it bundle/ 2>/dev/null || true
	cp -R .venv/lib/python*/site-packages/markdown_it_py bundle/ 2>/dev/null || true
	cp -R .venv/lib/python*/site-packages/mdurl bundle/ 2>/dev/null || true

	# create the zipapp; the shebang will use system python (or the one found via env)
	python3 -m zipapp bundle/ -o swb --python "/usr/bin/env python3" --compress
	chmod +x swb

clean:
	rm -rf bundle
