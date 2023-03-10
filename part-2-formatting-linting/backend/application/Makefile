#Makefile
format-black:
	poetry run black .

format-isort:
	poetry run isort .

lint-black:
	poetry run black . --check

lint-isort:
	poetry run isort . --check

lint-flake8:
	poetry run flake8

lint-mypy:
	poetry run mypy ./src

lint-mypy-report:
	poetry run mypy ./src --html-report ./mypy_html

format: format-black format-isort

lint: lint-black lint-isort lint-flake8 lint-mypy