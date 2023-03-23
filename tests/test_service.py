from unittest import TestCase
from get_cli.service import GetService
import get_cli.constants as c
import pyperclip
from tests.mocks import FileStorageMock




class TestGetCallback(TestCase):
    def setUp(self):
        self.storage = FileStorageMock(c.DEFAULT_STORAGE_DATA)
        self.service = GetService(self.storage)

    def test_get(self):
        result = self.service.get('hello')
        expected = 'world'
        self.assertEqual(result, expected)
        self.assertEqual(pyperclip.paste(), expected)

    def test_get_doesnt_exist(self):
        result = self.service.get('doesntexist')
        expected = None
        self.assertEqual(result, expected)

    def test_list_keys(self):
        self.storage.data = {'hello': 'world', 'hey': 'there'}
        result = self.service.list_keys()
        expected = 'hello, hey'
        self.assertEqual(result, expected)
        self.assertEqual(pyperclip.paste(), expected)

    def test_list_items(self):
        self.storage.data = {'hello': 'world', 'hey': 'there'}
        result = self.service.list_items()
        expected = 'hello: world\nhey: there'
        self.assertEqual(result, expected)
        self.assertEqual(pyperclip.paste(), expected)

    def test_update(self):
        data = {'hey': 'there', 'whats': 'up'}
        self.service.update(data)
        expected = data
        expected.update(c.DEFAULT_STORAGE_DATA)
        self.assertDictEqual(self.storage.data, expected)
