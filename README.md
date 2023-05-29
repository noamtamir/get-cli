# get-cli
A simple unsafe cli tool to store and fetch data locally.    
    
Need to fill in your parents zipcode on an online form?   
Need to paste your linkedin profile on a job application?   
Fetch them quickly from your terminal!    
The value will be copied to your clipboard, and you can paste it BLAZINGLY FAST! :)
## Dependencies
- python 3.8+

## Install
```shell
$ pip install get-cli
```

## Quick start
```properties
$ get hello

world
```

## Docs
```shell
Usage: get [OPTIONS] [KEY] COMMAND [ARGS]...

A simple unsafe tool to store and fetch values locally.                                                             
                                                                                                              
key [KEY] Retrieve value by key

Options
-------
--add  -a  TEXT  Create/update a key-value in the following format key:value. Batch support: -a key1:value1 -a key2:value2. Do not use colons (:) in your key names. Overrides if key already exists.
--list-keys  -lk,-l  List all keys
--list-items  -li  List all items (key-values)
--edit-with  -e  TEXT  Edit storage (.get.yml) with your favourite editor. Tested with vim, nano, code.

--install-completion  Install completion for the current shell.
--show-completion  Show completion for the current shell, to copy it or customize the installation.
--version  -v  Show the application's version
--help  Show this message and exit.
```

## Tested on
- macOS + Windows
- python 3.8+

Currently does not support linux, possible extra packages need to be installed: https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error


## Develop locally

### Setup environment
1. `brew install pyenv` [pyenv](https://github.com/pyenv/pyenv#installation)
2. `pyenv install 3.11` (or 3.8 and above)
3. [install poetry](https://python-poetry.org/docs/#installation)
4. `python -m venv .venv`
5. `source .venv/bin/activate`
6. `poetry install`

### Run
- Tests: `poetry run python -m unittest`
- Run: `poetry run python get_cli`
- Publish to pypi `poetry publish --build` (Don't forget to bump the version in `pyporject.toml`)