import get_cli.constants as c
import yaml
from pathlib import Path
from typing import Protocol
from subprocess import call

class Storage(Protocol):
    def __init__(self, filepath: Path = c.DEFAULT_STORAGE_PATH):
        ...

    def get(self, key: str) -> str | None:
        ...

    def list_keys(self) -> list[str]:
        ...

    def list_items(self) -> dict:
        ...
    
    def update(self, key_values: dict):
        ...

    def edit_with_editor(self, editor: str | None):
        ...

class FileStorage:
    def __init__(self, filepath: Path = c.DEFAULT_STORAGE_PATH, data: dict = c.DEFAULT_STORAGE_DATA):
        self.filepath = filepath
        self._load_data(data)

    def _load_data(self, data: dict | None = None):
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                self.data: dict = yaml.safe_load(f)
        elif data:
            self.data = self._create_storage_file(data)

    def _create_storage_file(self, data: dict) -> dict:
        with open(self.filepath, 'w') as f:
            yaml.safe_dump(data, f, sort_keys=True)
        return data

    def get(self, key: str) -> str | None:
        value = self.data.get(key)
        return str(value) if value else None

    def list_keys(self) -> list[str]:
        return list(self.data.keys())

    def list_items(self) -> dict:
        return self.data
    
    def update(self, key_values: dict):
        # create and/or update one or many key value pairs
        # overrides if key exists
        self.data.update(key_values)
        with open(self.filepath, 'w') as f:
            yaml.safe_dump(self.data, f, sort_keys=True)

    def edit_with_editor(self, editor: str = c.DEFAULT_EDITOR):
        call([editor, c.DEFAULT_STORAGE_PATH])
        self._load_data()