.DEFAULT_GOAL := help
.PHONY: clean pep257 pep8 test install dist

NOSETESTS       := nosetests
PEP257          := pep257
PEP8            := flake8
PIP             := pip

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;

pep257:
	$(PEP257) --ignore=D203,D302 habrahabr

pep8:
	$(PEP8) habrahabr

test:
	$(NOSETESTS) -v

install:
	$(PIP) install -r requirements-dev.txt

dist:
	python setup.py register
	python setup.py sdist bdist_wheel upload

help:
	@echo "Available targets:"
	@echo "- clean       Clean up the source directory"
	@echo "- pep257      Check docstring style with pep257"
	@echo "- pep8        Check style with flake8"
	@echo "- test        Run tests"
