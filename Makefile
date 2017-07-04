PYTHON := `which python`

NAME = cffi_demo_pkg
VERSION = $(shell $(PYTHON) -c 'import setup; print setup.VERSION')

.PHONY: package build develop install test clean

package:
	$(PYTHON) setup.py sdist --formats=gztar bdist_wheel

build:
	$(PYTHON) setup.py build

develop:
	$(PYTHON) setup.py develop

install:
	$(PYTHON) setup.py install

test:
	$(PYTHON) setup.py test

clean:
	$(PYTHON) setup.py clean
