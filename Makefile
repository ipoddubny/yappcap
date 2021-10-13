
PYTHON := python

all: yappcap.c
	$(PYTHON) setup.py build_ext

yappcap.c: yappcap.pyx definitions.pxi
	cython yappcap.pyx

definitions.pxi: generate_defs
	./generate_defs > definitions.pxi

generate_defs:
	cc -Wall -o generate_defs generate_defs.c -lpcap

clean:
	$(PYTHON) setup.py clean
	rm -f generate_defs definitions.pxi *.so

regen: clean
	rm -f yappcap.c
	make

install: all
	$(PYTHON) setup.py install

.PHONY: clean
.PHONY: install
