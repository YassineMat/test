# Project title

- [Project title](#project-title)
  - [Project Description](#project-description)
  - [Installation and setup](#installation-and-setup)
    - [Tests](#tests)
    - [Documentation](#documentation)
  - [Project template information](#project-template-information)
    - [Recommended VSCode extensions](#recommended-vscode-extensions)
    - [Tools used](#tools-used)

## Project Description

_Add your project description here_

## Installation and setup

To install project dependencies using poetry, run:
```bash
make install
```

To activate the shell containing these dependencies, run
```bash
make activate
```

### Tests

Write all your tests using in `tests/` following pytest's standard naming: `test_<something>.py`.
To manually run tests, run:
```bash
make tests
```
### Documentation

Write python documentation using python doc strings for every element of the code: file, function, class, methods, ...
These will be automatically generate the documentation in `docs/`, to see it in your browser on port 8080, run:
```bash
make docs
```

## Project template information

### Recommended VSCode extensions

Install these recommended VSCode extensions by searching for them using their ids in the in the `extensions` tab of VSCode.

- Spell checker: streetsidesoftware.code-spell-checker
- Docker: ms-azuretools.vscode-docker
- Markdown: yzhang.markdown-all-in-one
- YAML: redhat.vscode-yaml
- Python: ms-python.python

### Tools used

- pipx: Install Python CLI packages (like poetry).
- poetry: Manage python dependencies (replaces requirements.txt), see `./pyproject.toml`.
- pre-commit: A set of checks that are done automatically before any commit, see `./.pre-commit-config.yaml`.
- Makefile: Have simple command, see `./Makefile`.
- Hydra: Configuration management for Python projects, see `./config/`.
- black: Python formatter.
- ruff: Python linter.
- mypy: Python static type checker.
- pytest: Python test library.
- pdoc: Automatically generate documentation in HTML from Python doc strings, see `./docs/`.
- dvc: A data version control tool.
