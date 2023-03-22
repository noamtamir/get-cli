import os
from typer.testing import CliRunner
from pathlib import Path
from unittest import TestCase
import get_cli.constants as c
from get_cli import __app_name__, __version__
from get_cli.cli import create_app
from get_cli.controller import GetController
from get_cli.service import GetService
from get_cli.storage import FileStorage

runner = CliRunner()


class TestGetCli(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filepath = Path.cwd() / '.get.e2e.yml'
        data = c.DEFAULT_STORAGE_DATA
        data.update({'hey': 'there', 'whats': 'up'})
        cls.storage = FileStorage(cls.filepath, data)
        cls.service = GetService(cls.storage)
        cls.controller = GetController(cls.service)
        cls.app = create_app(cls.controller)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filepath)

    def test_version(self):
        result = runner.invoke(self.app, ["--version"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(f"{__app_name__} v{__version__}\n", result.stdout)

    def test_get(self):
        result = runner.invoke(self.app, ["hello"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual("world\n", result.stdout)

    def test_get_not_found(self):
        result = runner.invoke(self.app, ["doesntexist"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual("Not found\n", result.stdout)

    def test_list_keys(self):
        result = runner.invoke(self.app, ["-lk"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual("hello, hey, whats\n", result.stdout)

    def test_list_items(self):
        result = runner.invoke(self.app, ["-li"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(
            "hello: world\nhey: there\nwhats: up\n", result.stdout)

    def test_update(self):
        result = runner.invoke(self.app, ['-a', 'hey:ho', '-a', 'abc:123'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual("Success!\n", result.stdout)

        hey_value = self.storage.data.get('hey')
        abc_value = self.storage.data.get('abc')
        self.assertEqual(hey_value, 'ho')
        self.assertEqual(abc_value, '123')

    def test_update_illegal(self):
        result = runner.invoke(self.app, ['-a', 'heyho', '-a', 'abc123'])
        self.assertEqual(result.exit_code, 1)

    # TODO: mock editor
    # def test_edit_with_editor(self):
    #     result = runner.invoke(self.app, ['-e', 'vim'])
    #     self.assertEqual(result.exit_code, 0)