include .env
export


SHELL := /bin/bash
PYTHON_SOURCES = gh_automation_base/
DSN := postgresql+psycopg://${GH_AUTO_PG_USER}:${GH_AUTO_PG_PASSWORD}@${GH_AUTO_PG_AIVEN_SERVICE}-${GH_AUTO_PG_AIVEN_PROJECT}.aivencloud.com:${GH_AUTO_PG_PORT}/${GH_AUTO_PG_DATABASE}?sslmode=require


install:
	poetry install

format-check:
	poetry run ruff check $(PYTHON_SOURCES)
	poetry run black --check $(PYTHON_SOURCES)
	poetry run mypy $(PYTHON_SOURCES)

format:
	poetry run ruff check $(PYTHON_SOURCES) --fix
	poetry run black $(PYTHON_SOURCES)
	poetry run mypy $(PYTHON_SOURCES)

migration-init:
	rm -f yoyo.ini
	poetry run yoyo init --database $(DSN) migrations

migration-new:
	poetry run yoyo new --sql --database $(DSN) --batch

migration-apply:
	poetry run yoyo apply --database $(DSN) --batch

migration-list:
	poetry run yoyo list --database $(DSN)
