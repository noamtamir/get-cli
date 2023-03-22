# get-cli
A simple unsafe cli tool to store and fetch data locally.    
Need to fill in your parents zipcode on an online form? Need to paste your linkedin profile on a job application? Fetch them quickly from your terminal! The value will be copied to your clipboard, and you can paste it BLAZINGLY FAST! :)

## Install and setup
...

## Quick start
```properties
$ python -m get_cli hello

world
```

## Docs
```shell
Usage: get-cli [OPTIONS] [KEY] COMMAND [ARGS]...

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

## Misc
- Used python 3.11.2 to develop