""" 
Backend Operation Unit Tests
"""
import sys
import os
import unittest
from unittest.mock import patch
from datetime import datetime
import random

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(project_root)

from src.data.record_manager import RecordManager

class TestRecordManager(unittest.TestCase):
    """CRUD Test Cases"""

    def setUp(self):
        """Set up the initial conditions for each test."""
        self.record_manager = RecordManager(
            data_folder="mock_data", file_format="jsonl")

    def generate_random_client(self):
        """Generate random client data."""
        return {
            "id": f"C{random.randint(1000, 9999)}",
            "type": "Client",
            "name": f"Client_{random.choice(['A', 'B', 'C', 'D'])}{random.randint(1, 100)}",
            "email": f"client{random.randint(1, 100)}@example.com",
            "phone": f"+1{random.randint(1000000000, 9999999999)}",
            "address_line1": f"{random.randint(1, 999)} {random.choice(['Main St', 'Park Ave', 'Broadway'])}",
            "address_line2": f"Suite {random.randint(100, 999)}",
            "address_line3": f"Floor {random.randint(1, 20)}",
            "city": random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']),
            "state": random.choice(['NY', 'CA', 'IL', 'TX', 'AZ']),
            "zip_code": f"{random.randint(10000, 99999)}",
            "country": random.choice(['United States', 'Canada', 'United Kingdom', 'Australia']),
            "created_at": datetime.now().isoformat()
        }

    def generate_random_flight(self):
        """Generate random flight data based on add_new_flight form fields."""

        # Helper function for date format
        def random_date():
            day = str(random.randint(1, 28)).zfill(2)
            month = str(random.randint(1, 12)).zfill(2)
            year = str(random.randint(2023, 2024))
            return f"{day}/{month}/{year}"

        # List of sample cities
        cities = ['New York', 'London', 'Tokyo', 'Paris', 'Dubai',
                  'Singapore', 'Hong Kong', 'Sydney', 'Toronto']

        # Generate two different cities
        from_city, to_city = random.sample(cities, 2)

        return {
            "id": f"F{random.randint(1000, 9999)}",
            "type": "Flight",
            "client": f"Client_{random.choice(['A', 'B', 'C', 'D'])}{random.randint(1, 100)}",
            "airline": f"{random.choice(['British Airways', 'Cathay Pacific Airways', 'Qantas Airways'])}",
            "departure": from_city,
            "destination": to_city,
            "depart_date": random_date(),
            # Optional return date
            "return_date": random_date() if random.choice([True, False]) else "",
            "created_at": datetime.now().isoformat()
        }

    def generate_random_airline(self):
        """Generate random airline data."""
        return {
            "id": f"A{random.randint(100, 999)}",
            "type": "Airline",
            "company_name": f"Airline_{random.choice(['X', 'Y', 'Z'])}",
            "country": random.choice(['United States', 'Canada', 'United Kingdom', 'Australia']),
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

        self.record_manager.update_record(
            "client", random_client['id'], updated_client)

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

    @patch.object(RecordManager, 'save_records')
    def test_add_flight(self, mock_save):
        """Test adding a random flight record."""
        # Generate random flight
        random_flight = self.generate_random_flight()

        # Add the random flight record
        self.record_manager.add_record("flight", random_flight)

        # Check that save was called once
        self.assertEqual(mock_save.call_count, 1)
        mock_save.assert_called_once()

    @patch.object(RecordManager, 'save_records')
    def test_update_flight(self, mock_save):
        """Test updating a random flight record."""
        # Add a random flight
        random_flight = self.generate_random_flight()
        self.record_manager.add_record("flight", random_flight)

        # Update the flight with random new data
        updated_flight = random_flight.copy()
        updated_flight['departure'] = "Updated_" + random_flight['departure']
        updated_flight['destination'] = "Updated_" + \
            random_flight['destination']

        self.record_manager.update_record(
            "flight", random_flight['id'], updated_flight)

        # Assert that save was called twice (once for adding, once for updating)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()

    @patch.object(RecordManager, 'save_records')
    def test_delete_flight(self, mock_save):
        """Test deleting a random flight record."""
        # Add a random flight
        random_flight = self.generate_random_flight()
        self.record_manager.add_record("flight", random_flight)

        # Delete the random flight
        self.record_manager.delete_record("flight", random_flight['id'])

        # Assert that save was called twice (once for adding, once for deleting)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()

    @patch.object(RecordManager, 'save_records')
    def test_add_airline(self, mock_save):
        """Test adding a random airline record."""
        # Generate random airline
        random_airline = self.generate_random_airline()

        # Add the random airline record
        self.record_manager.add_record("airline", random_airline)

        # Check that save was called once
        self.assertEqual(mock_save.call_count, 1)
        mock_save.assert_called_once()

    @patch.object(RecordManager, 'save_records')
    def test_update_airline(self, mock_save):
        """Test updating a random airline record."""
        # Add a random airline
        random_airline = self.generate_random_airline()
        self.record_manager.add_record("airline", random_airline)

        # Update the airline with random new data
        updated_airline = random_airline.copy()
        updated_airline['company_name'] = f"Updated_{random_airline['company_name']}"

        self.record_manager.update_record(
            "airline", random_airline['id'], updated_airline)

        # Assert that save was called twice (once for adding, once for updating)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()

    @patch.object(RecordManager, 'save_records')
    def test_delete_airline(self, mock_save):
        """Test deleting a random airline record."""
        # Add a random airline
        random_airline = self.generate_random_airline()
        self.record_manager.add_record("airline", random_airline)

        # Delete the random airline
        self.record_manager.delete_record("airline", random_airline['id'])

        # Assert that save was called twice (once for adding, once for deleting)
        self.assertEqual(mock_save.call_count, 2)
        mock_save.assert_any_call()


if __name__ == "__main__":
    unittest.main(verbosity=2)
