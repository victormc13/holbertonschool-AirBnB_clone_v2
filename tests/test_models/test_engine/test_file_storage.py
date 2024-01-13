#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """ Remove storage file at the end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        key = f'{new.__class__.__name__}.{new.id}'
        self.storage.new(new)
        self.assertIn(key, self.storage.all())

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        self.storage.new(new)
        temp = self.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        self.storage.new(new)
        self.storage.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.storage.reload()
        key = list(self.storage.all().keys())[0]
        self.assertIn(key, self.storage.all())

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            self.storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if the file does not exist """
        self.assertEqual(self.storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        self.storage.new(new)
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is a string """
        self.assertEqual(type(self.storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(self.storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        self.storage.new(new)
        temp = list(self.storage.all().keys())[0]
        self.assertTrue(temp.startswith(new.__class__.__name__))

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        self.assertEqual(type(self.storage), FileStorage)


if __name__ == '__main__':
    unittest.main()
