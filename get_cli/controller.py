import typer
from typing import Protocol
from get_cli.service import Service
from get_cli import __app_name__, __version__


class Controller(Protocol):
    def __init__(self, service: Service):
        ...

    def get_version(flag: bool):
        ...

    def get(key: str):
        ...

    def list_keys(flag: bool):
        ...

    def list_items(flag: bool):
        ...

    def update(key_values: list[str]):
        ...

    def edit_with_editor(editor: str):
        ...


class GetController:
    def __init__(self, service: Service):
        self.service = service

    def get_version(self, flag: bool):
        if flag:
            print(f"{__app_name__} v{__version__}")
            raise typer.Exit()

    def get(self, key: str):
        if key:
            value = self.service.get(key)
            if not value:
                print('Not found')
                raise typer.Exit()
            print(value)
        raise typer.Exit()

    def list_keys(self, flag: bool):
        if flag:
            print(self.service.list_keys())
        raise typer.Exit()

    def list_items(self, flag: bool):
        if flag:
            print(self.service.list_items())
        raise typer.Exit()

    def update(self, key_values: list[str]):
        if key_values:
            data = dict([i.split(':') for i in key_values])
            try:
                self.service.update(data)
                print('Success!')
            except:
                print('Fail...')
        raise typer.Exit()

    def edit_with_editor(self, editor: str):
        self.service.edit_with_editor(editor)
        raise typer.Exit()
