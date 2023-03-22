import typer
import pyperclip
from get_cli import __app_name__, __version__
from get_cli.storage import Storage
from typing import Protocol

class Service(Protocol):
    def __init__(self, storage: Storage):
        ...

    def get(self, key: str) -> str | None:
        ...

    def list_keys(self) -> str:
        ...

    def list_items(self) -> str:
        ...
    
    def update(self, key_values: dict):
        ...

class GetService:
    def __init__(self, storage: Storage):
        self.storage = storage
    
    def get(self, key: str) -> str | None:
        value = self.storage.get(key)
        if value:
            pyperclip.copy(value)
        return value

    def list_keys(self) -> str:
        keys = self.storage.list_keys()
        keys_str = ', '.join(keys)
        pyperclip.copy(keys_str)
        return keys_str

    def list_items(self) -> str:
        items = self.storage.list_items()
        keys_str = '\n'.join([f'{k}: {v}' for k, v in items.items()])
        pyperclip.copy(keys_str)
        return keys_str

    def update(self, key_values: dict):
        self.storage.update(key_values)


    def edit_with_editor(self, editor: str | None):
        self.storage.edit_with_editor(editor)
