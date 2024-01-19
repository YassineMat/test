.PHONY: shell test clean

venv_bin=.venv/bin

# REMPLACER `template` LE NOM DE VOTRE PROJET
project_name=template

devc-up:
	@echo "\nCreating developpment container..."
	mkdir containers/cache
	cp -r -t containers/cache ~/.gitconfig ~/.ssh
	docker compose -f containers/docker-compose.dev.yaml up -d
	rm -r containers/cache

devc-down:
	@echo "\nDestroying developpment container..."
	docker compose -f containers/docker-compose.dev.yaml down

devc-stop:
	@echo "\nStopping developpment container..."
	docker compose -f containers/docker-compose.dev.yaml stop

devc-start:
	@echo "\nStarting developpment container..."
	docker compose -f containers/docker-compose.dev.yaml start

devc-enter:
	@echo "\nEntering developpment container..."
	docker exec -it devc-$(project_name)-$$USER bash

devc-logs:
	@echo "\nLogging developpment container..."
	docker logs -f devc-$(project_name)-$$USER bash

install:
	python3 -m venv .venv
	@echo "Installing dependencies..."
# Install project dependencies using pip
	$(venv_bin)/pip install -r requirements.txt
# Install pre-commit dependencies
	$(venv_bin)/pre-commit install
	@echo "\nTo activate virtualenv, run 'source $(venv_bin)/activate'.\n"

shell:
	@echo "\nTo activate virtualenv, run 'source $(venv_bin)/activate'.\n"

test:
	PYTHONPATH=src $(venv_bin)/pytest

doc:
	@echo "\nGenerating documentation..."
	PYTHONPATH=src $(venv_bin)/pdoc -d google -o docs src/*
	@echo "\nDocumentation generated at docs/html."

doc-server:
	@echo "\nRunning pdoc documentation server..."
	PYTHONPATH=src $(venv_bin)/pdoc -d google -h 0.0.0.0 -p 8080 src/*

pre-commit:
	$(venv_bin)/pre-commit run --all-files

run:
	$(venv_bin)/python3 src/main.py

clean:
	@echo "Cleaning python cache..."
# Python cache files
	rm -rf src/__pycache__/
	rm -rf src/*/__pycache__/
# Pytest cache files
	@echo "\nCleaning pytest cache..."
	rm -rf .pytest_cache/
# Ruff cache files
	@echo "\nCleaning ruff cache..."
	rm -rf .ruff_cache/
