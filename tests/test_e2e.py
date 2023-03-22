from typer.testing import CliRunner
from unittest import TestCase
from unittest.mock import patch
from get_cli import __app_name__, __version__
from get_cli.cli import create_app
from tests.mocks import FileStorageMock
import get_cli.constants as c

runner = CliRunner()


# class TestGetCli(TestCase):
    # e2e test
    # TODO: mock FileStorage when instantiating app
    # def test_version(self):
    #     result = runner.invoke(app, ["--version"])
    #     self.assertEqual(result.exit_code, 0)
    #     self.assertEqual(f"{__app_name__} v{__version__}\n", result.stdout)
