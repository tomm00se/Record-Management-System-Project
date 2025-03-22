import unittest
import os
import json
import pickle
import shutil
from src.data.record_manager import RecordManager

class TestRecordManager(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.test_folder = "test_data"
        self.test_format = "json"
        self.manager = RecordManager(data_folder=self.test_folder, file_format=self.test_format)
        self.sample_record = {"id": "123", "name": "Test Client"}
        self.manager.records["client"].append(self.sample_record)
        self.manager.save_records()

    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)  # Remove the entire folder and its contents

    def test_load_records(self):
        """Test if records are loaded correctly."""
        new_manager = RecordManager(data_folder=self.test_folder, file_format=self.test_format)
        self.assertIn(self.sample_record, new_manager.records["client"])

    def test_save_records(self):
        """Test if records are saved correctly."""
        file_path = self.manager._get_file_path("client")
        with open(file_path, "r") as file:
            data = json.load(file)
        self.assertIn(self.sample_record, data)

    def test_get_file_path(self):
        """Test file path generation."""
        expected_path = os.path.join(self.test_folder, "client.json")
        self.assertEqual(self.manager._get_file_path("client"), expected_path)

if __name__ == "__main__":
    unittest