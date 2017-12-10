.PHONY: all
all: test build

.PHONY: build
build:
	python setup.py sdist build install

.PHONY: test
test:
	python setup.py test
