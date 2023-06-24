PYTHON_SOURCES = gh_automation_base/

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
