.PHONY: all env install nopyc clean test

SHELL := /usr/bin/env bash
PYTHON_BIN ?= python
PROJECT_VENV ?= venv

all: test

env:
	cp -n .env.example .env | true

venv: env
	$(PYTHON_BIN) -m pip install virtualenv --user
	$(PYTHON_BIN) -m virtualenv $(PROJECT_VENV)

install: env venv
	@( \
		source $(PROJECT_VENV)/bin/activate; \
		python -m pip install -r requirements.txt; \
	)

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

clean: nopyc
	rm -rf $(PROJECT_VENV)

test: install
	@( \
		source $(PROJECT_VENV)/bin/activate; \
		python -m unittest discover; \
	)
