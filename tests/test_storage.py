from unittest import TestCase
from get_cli.storage import FileStorage
from pathlib import Path
import os
import yaml
import get_cli.constants as c


class TestStorageInit(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.filepath = Path.cwd() / '.test.storage.init.yml'

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.filepath)

    def test_init_and_load(self):
        # test creating storage
        storage = FileStorage(self.filepath)
        self.assertEqual(storage.data, c.DEFAULT_STORAGE_DATA)
        self.assertTrue(self.filepath.exists())
        # test loading storage
        storage_2 = FileStorage(self.filepath)
        self.assertEqual(storage_2.data, c.DEFAULT_STORAGE_DATA)
        self.assertTrue(self.filepath.exists())


class TestStorage(TestCase):
    def setUp(self):
        self.filepath = Path.cwd() / '.test.storage.yml'
        self.storage = FileStorage(self.filepath)

    def tearDown(self):
        os.remove(self.filepath)

    def test_a_get(self):
        # weird name because of test alphabetical order in unittest.
        # for some reason setup/teardown not functioning correctly.
        result = self.storage.get('hello')
        expected = 'world'
        self.assertEqual(result, expected)

    def test_get_doesnt_exist(self):
        result = self.storage.get('doesntexist')
        expected = None
        self.assertEqual(result, expected)

    def test_create_one(self):
        data = {'testing': 123}
        self.storage.update(data)
        expected = data
        expected.update(c.DEFAULT_STORAGE_DATA)
        self.assertEqual(self.storage.data, expected)
        with open(self.filepath, 'r') as f:
            result: dict = yaml.safe_load(f)
        self.assertEqual(result, expected)

    def test_create_many(self):
        data = {'testing': 123, 'hey': 'there'}
        self.storage.update(data)
        expected = data
        expected.update(c.DEFAULT_STORAGE_DATA)
        self.assertEqual(self.storage.data, expected)
        with open(self.filepath, 'r') as f:
            result: dict = yaml.safe_load(f)
        self.assertEqual(result, expected)

    def test_create_and_update(self):
        data = {'testing': 123, 'hello': 'there'}
        self.storage.data = {'hello': 'world'}
        self.storage.update(data)
        expected = data
        self.assertEqual(self.storage.data, expected)
        with open(self.filepath, 'r') as f:
            result: dict = yaml.safe_load(f)
        self.assertEqual(result, expected)

    def test_list_keys(self):
        self.storage.data = {'testing': 123, 'hey': 'there'}

        result = self.storage.list_keys()
        expected = ['testing', 'hey']

        self.assertListEqual(result, expected)

    def test_list_items(self):
        data = {'testing': 123, 'hey': 'there'}
        self.storage.update(data)

        result = self.storage.list_items()
        expected = data
        expected.update(c.DEFAULT_STORAGE_DATA)
        self.assertDictEqual(result, expected)
