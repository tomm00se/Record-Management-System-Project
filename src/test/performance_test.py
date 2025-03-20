import time
import random
from src.data.record_manager import RecordManager

class PerformanceTest:
    def __init__(self, record_manager: RecordManager):
        self.record_manager = record_manager

    def generate_random_client(self):
        """Generate random client data."""
        return {
            "id": f"C{random.randint(1000, 9999)}",
            "name": f"Client_{random.choice(['A', 'B', 'C', 'D'])}{random.randint(1, 100)}",
            "email": f"client{random.randint(1, 100)}@example.com",
            "phone": f"+1{random.randint(1000000000, 9999999999)}",
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S")
        }

    def benchmark_add_records(self, num_records: int = 1000):
        """Benchmark the time taken to add multiple records."""
        start_time = time.time()

        for _ in range(num_records):
            random_client = self.generate_random_client()
            self.record_manager.add_record("client", random_client)

        end_time = time.time()
        print(f"Added {num_records} client records in {end_time - start_time:.4f} seconds.")

    def benchmark_update_record(self, record_id: str = None):
        """Benchmark the time taken to update a record."""
        # If no specific record_id is provided, select an existing record ID dynamically.
        if not record_id:
            record_id = self.record_manager.records["client"][random.randint(0, len(self.record_manager.records["client"]) - 1)]["id"]

        random_client = self.generate_random_client()  # Generate a new client
        updated_client = random_client.copy()
        updated_client['name'] = f"Updated_{random_client['name']}"

        start_time = time.time()
        try:
            self.record_manager.update_record("client", record_id, updated_client)
            end_time = time.time()
            print(f"Updated record {record_id} in {end_time - start_time:.4f} seconds.")
        except ValueError as e:
            print(str(e))

    def benchmark_delete_record(self, record_id: str):
        """Benchmark the time taken to delete a record."""
        start_time = time.time()
        self.record_manager.delete_record("client", record_id)
        end_time = time.time()

        print(f"Deleted record {record_id} in {end_time - start_time:.4f} seconds.")

    def benchmark_load_records(self):
        """Benchmark the time taken to load records."""
        start_time = time.time()
        self.record_manager.load_records()
        end_time = time.time()

        print(f"Loaded records in {end_time - start_time:.4f} seconds.")

    def benchmark_save_records(self):
        """Benchmark the time taken to save records."""
        start_time = time.time()
        self.record_manager.save_records()
        end_time = time.time()

        print(f"Saved records in {end_time - start_time:.4f} seconds.")

# Example Usage
if __name__ == "__main__":
    # Initialize RecordManager
    record_manager = RecordManager(data_folder="mock_data", file_format="jsonl")

    # Run performance tests
    performance_test = PerformanceTest(record_manager)

    # Add 1000 records to test
    performance_test.benchmark_add_records(num_records=1000)
    # Load records from the file system
    performance_test.benchmark_load_records()
    # Update a record (either a random one or a specified ID)
    performance_test.benchmark_update_record()  # Automatically selects a random record
    # Delete a record (assuming you have a record with ID 'C1001')
    performance_test.benchmark_delete_record(record_id="C1001")
    # Save records to the file system
    performance_test.benchmark_save_records()
