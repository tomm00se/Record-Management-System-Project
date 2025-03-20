import unittest
from unittest.mock import patch
from datetime import datetime
import random
import string
from src.data.record_manager import RecordManager  # Adjust the import as needed

class TestRecordManager(unittest.TestCase):

    def setUp(self):
        """Set up the initial conditions for each test."""
        self.record_manager = RecordManager(data_folder="mock_data", file_format="jsonl")

    def generate_random_client(self):
        """Generate random client data."""
        return {
            "id": f"C{random.randint(1000, 9999)}",
            "name": f"Client_{random.choice(['A', 'B', 'C', 'D'])}{random.randint(1, 100)}",
            "email": f"client{random.randint(1, 100)}@example.com",
            "phone": f"+1{random.randint(1000000000, 9999999999)}",
            "created_at": datetime.now().isoformat()
        }

    def generate_random_flight(self):
        """Generate random flight data."""
        return {
            "id": f"F{random.randint(1000, 9999)}",
            "airline_id": f"A{random.randint(100, 999)}",
            "departure": f"City_{random.choice(['X', 'Y', 'Z'])}",
            "destination": f"City_{random.choice(['A', 'B', 'C'])}",
            "flight_date": datetime.now().isoformat(),
            "status": random.choice(['on time', 'delayed', 'cancelled']),
            "created_at": datetime.now().isoformat()
        }

    def generate_random_airline(self):
        """Generate random airline data."""
        return {
            "id": f"A{random.randint(100, 999)}",
            "name": f"Airline_{random.choice(['X', 'Y', 'Z'])}",
            "iata_code": ''.join(random.choices(string.ascii_uppercase, k=3)),
            "created_at": datetime.now().isoformat()
        }

    @patch.object(RecordManager, 'save_records')
    def test_add_client(self, mock_save):
        """Test adding a random client record."""
        # Generate random client
        random_client = self.generate_random_client()

        # Add the random client record
        self.record_manager.add_record("client", random_client)

        # Check that save was called once
        self.assertEqual(mock_save.call_count, 1)
        mock_save.assert_called_once()

    @patch.object(RecordManager, 'save_records')
    def test_update_client(self, mock_save):
        """Test updating a random client record."""
        # Add a random client
        random_client = self.generate_random_client()
        self.record_manager.add_record("client", random_client)

        # Update the client with random new data
        updated_client = random_client.copy()
        updated_client['name'] = f"Updated_{random_client['name']}"
        updated_client['email'] = f"updated_{random_client['email']}"

        self.record_manager.update_record("client", random_client['id'], updated_client)

        # Assert that save was called twice (once for adding, once for updating)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()

    @patch.object(RecordManager, 'save_records')
    def test_delete_client(self, mock_save):
        """Test deleting a random client record."""
        # Add a random client
        random_client = self.generate_random_client()
        self.record_manager.add_record("client", random_client)

        # Delete the random client
        self.record_manager.delete_record("client", random_client['id'])

        # Assert that save was called twice (once for adding, once for deleting)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()

if __name__ == "__main__":
    unittest.main()
