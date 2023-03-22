from get_cli.controller import GetController
from get_cli.service import GetService
from get_cli.storage import FileStorage
from get_cli.cli import create_app
from get_cli import __app_name__



# instantiate IoC and run app
storage = FileStorage()
service = GetService(storage)
controller = GetController(service)
app = create_app(controller)
