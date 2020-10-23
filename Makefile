default : clean dist

dist :
	python setup.py sdist --formats=gztar,zip
	python setup.py bdist_wheel --python-tag=py3

clean :
	find . -name "*pyc" | xargs rm -rf $1
	rm -rf build dist bundle MANIFEST htmlcov deb_dist swb*.tar.gz swb.1.man

bundle:
	mkdir bundle
	cp strawberry/__main__.py bundle
	pip install . --target=bundle
	rm -rf bundle/*.dist-info
	find bundle/ -type d -name "__pycache__" -exec rm -rf {} +
	python -m zipapp \
		--python "/usr/bin/env python3" \
		--output swb.`git describe`.pyz bundle \
		--compress

publish :
	twine upload dist/*.tar.gz dist/*.whl

coverage:
	py.test --cov=toot --cov-report html tests/

deb:
	@python3 setup.py --command-packages=stdeb.command bdist_deb
