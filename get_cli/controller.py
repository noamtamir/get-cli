import typer
from get_cli.service import GetService
from get_cli.storage import FileStorage
from get_cli import __app_name__, __version__

# init IoC
storage = FileStorage()
service = GetService(storage)

# controller (cli callbacks)
def get_version(flag: bool):
    if flag:
        print(f"{__app_name__} v{__version__}")
        raise typer.Exit()

def get(key: str):
    if key:
      value = service.get(key)
      if not value:
          print('Not found')
          raise typer.Exit()
      print(value)
    raise typer.Exit()

def list_keys(flag: bool):
    if flag:
      print(service.list_keys())
    raise typer.Exit()

def list_items(flag: bool):
    if flag:
      print(service.list_items())
    raise typer.Exit()

def update(key_values: list[str]):
    if key_values:
      data = dict([i.split(':') for i in key_values])
      try:
        service.update(data)
        print('Success!')
      except:
          print('Fail...')
    raise typer.Exit()


def edit_with_editor(editor: str | None):
    service.edit_with_editor(editor)
    raise typer.Exit()