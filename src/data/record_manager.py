import datetime
import os
import json
import pickle
from typing import List, Dict, Any, Optional, Literal

class RecordManager:
    """Manage records for client, flights and airline companies. Handles CRUD operations and File Persistence."""
    
    RECORD_TYPES = ['client', 'flight', 'airline']
    
    def __init__(self, data_folder: str = "records", file_format: str = "jsonl"):
        """Initialize RecordManager with data folder and file format."""
        
        self.data_folder = data_folder
        self.file_format = file_format.lower()
        
        # Check if file format is supported
        if self.file_format not in ['jsonl', 'json', 'pickle']:
            raise ValueError(f"File format '{self.file_format}' is not supported.")
        
        # Create data folder if it does not exist
        os.makedirs(self.data_folder, exist_ok=True)
        
        # Initialize records dictionary
        self.records = {
            "client": [],
            "flight": [],
            "airline": []
        }
        
        # Load records from files
        self.load_records()
        
    def _get_file_path(self, record_type: str):
        """Get file path for record type."""
        extention = self.file_format if self.file_format != 'jsonl' else 'json'
        # Return file path as formatted string using record type for file extension.
        return os.path.join(self.data_folder, f"{record_type}.{extention}")
    
    def load_records(self) -> None:
        """Load all records from files."""
        for record_type in self.records.keys():
            if record_type:
                file_path = self._get_file_path(record_type)
                if not os.path.exists(file_path):
                    continue
            
            try:
                if self.file_format == 'jsonl':
                    self.records[record_type] = []
                    with open(file_path, 'r') as file:
                        for line in file:
                            if line.strip(): # Check if line is not empty & strip whitespace
                                self.records[record_type].append(json.loads(line))
                
                elif self.file_format == 'json':
                    with open(file_path, 'r') as file:
                        self.records[record_type] = json.load(file)
                        
                elif self.file_format == 'pickle':
                    with open(file_path, 'rb') as file:
                        self.records[record_type] = pickle.load(file)
            
            except Exception as e:
                print(f"Error loading {record_type} records: {e}")
                self.records[record_type] = []
                
    def save_records(self) -> None:
        """Save all records to files."""
        for record_type, records in self.records.items():
            file_path = self._get_file_path(record_type)
            
            try:
                if self.file_format == 'jsonl':
                    with open(file_path, 'w') as file:
                        for record in records:
                            file.write(json.dumps(record) + '\n')
                            
                elif self.file_format == 'json':
                    with open(file_path, 'w') as file:
                        json.dump(records, file, indent=4)
                
                elif self.file_format == 'pickle':
                    with open(file_path, 'wb') as file:
                        pickle.dump(records, file)
                
            except Exception as e:
                print(f"Error saving {record_type} records: {e}")
    
    def add_record(self, record_type: str, new_record: Dict[str, Any]) -> None:
        """Add new records to existing records."""
        if record_type not in self.RECORD_TYPES:
            raise ValueError(f"Record type '{record_type}' is not supported.")
        
        last_record_id = self.records[record_type][-1]['id'] if self.records[record_type] else 'F0000'
        new_record_id = int(last_record_id[1:]) + 1
        new_record['id'] = f"{record_type.upper()[0]}{new_record_id:04d}"
        new_record['created_at'] = datetime.datetime.now().isoformat()
        
        new_records = [new_record]
        
        self.records[record_type].extend(new_records)
        self.save_records()
        
    def update_record(self, record_type: str, record_id: int, updated_record: Dict[str, Any]) -> None:
        """Update a record by ID."""
        if record_type not in self.RECORD_TYPES:
            raise ValueError(f"Record type '{record_type}' is not supported.")
        
        for i, record in enumerate(self.records[record_type]):
            if record['id'] == record_id:
                self.records[record_type][i] = updated_record
                self.save_records()
                return
        
        raise ValueError(f"Record with ID '{record_id}' not found in '{record_type}' records.")    
        
    def delete_record(self, record_type: str, record_id: int) -> None:
        """Delete record by ID."""
        if record_type not in self.RECORD_TYPES:
            raise ValueError(f"Record type '{record_type}' is not supported.")
        
        self.records[record_type] = [record for record in self.records[record_type] if record['id'] != record_id]
        self.save_records()