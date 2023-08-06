prepare:
	python -m pip install build twine
build: prepare
	python3 -m build
install:
	pip3 install -e .
clean:
	rm -rf test-molecule/
	rm -rf dist/
publish: clean build
# python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

.PHONY: test-molecule

test-molecule: clean
	mkdir test-molecule && \
	cd test-molecule && \
	ansible-galaxy role init test && \
	cd test && \
	molecule init scenario -d molecule-driver-azure && \
	sed -i '' -e 's/platforms:/bar/g' $(find ./test-molecule -name "molecule.yml")