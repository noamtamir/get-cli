from typing import Optional, List
import typer
from get_cli import __app_name__, __version__
from get_cli.controller import get, get_version, list_items, list_keys, update, edit_with_editor
import get_cli.constants as c

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main(
    key: Optional[str] = typer.Argument(
        None, help="Retrieve value by key", callback=get),
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version",
        callback=get_version,
        is_eager=True,
    ),
    list_keys: Optional[bool] = typer.Option(
        None,
        "--list-keys",
        "-lk",
        '-l',
        help='List all keys',
        callback=list_keys
    ),
    list_items: Optional[bool] = typer.Option(
        None,
        "--list-items",
        '-li',
        help='List all items (key-values)',
        callback=list_items
    ),
    new: List[str] = typer.Option(
        ...,
        "--add",
        "-a",
        help='Create/update a key-value in the following format key:value. Batch support: -a key1:value1 -a key2:value2. Do not use colons (:) in your key names. Overrides if key already exists.',
        callback=update
    ),
    edit: Optional[str] = typer.Option(
        None,
        "--edit-with",
        "-e",
        help='Edit storage (.get.yml) with your favourite editor. Tested with vim, nano, code.',
        callback=edit_with_editor
    )
) -> None:
    '''
    A simple unsafe tool to store and fetch values locally.
    '''
    return
