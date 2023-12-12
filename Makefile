.PHONY: all env install

PYTHON_BIN := python3
SHELL := /usr/bin/env bash

all: env virtualenv install

env:
	cp -n .env.example .env | true

virtualenv: env
	@if [ ! -d ".venv" ]; then \
		$(PYTHON_BIN) -m pip install virtualenv --user; \
		$(PYTHON_BIN) -m virtualenv .venv; \
	fi

install: env virtualenv
	@( \
		source .venv/bin/activate; \
		python -m pip install -r requirements.txt; \
	)

test: env virtualenv
	@( \
		source .venv/bin/activate; \
		python -m unittest discover; \
	)
