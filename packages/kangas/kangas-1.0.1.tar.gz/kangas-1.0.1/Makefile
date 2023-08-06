test::
	pytest -vvv tests

clean::
	rm -fr *.datagrid dist build

build::
	cd ../comet-datagrid; yarn build
	rm -rf datagrid/frontend
	cp -rf ../comet-datagrid/.next datagrid/frontend
	rm -rf datagrid/frontend/cache/*

update-frontend::
	git add datagrid/frontend
	git commit -m "Updated frontend"

wheel::
	python -m build --wheel

bdist::
	python setup.py bdist

sdist::
	python setup.py sdist

