import sys
from os.path import dirname, abspath, join
import tkinter as tk
from tkinter import messagebox
import json

# Add the parent directory to the system path
sys.path.append(abspath(join(dirname(__file__), '..')))

from data.record_manager import RecordManager

class RecordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Record Manager")

        self.record_manager = RecordManager(data_folder="src/record", file_format="json")

        # Create widgets
        self.record_type_label = tk.Label(root, text="Record Type:")
        self.record_type_label.grid(row=0, column=0)
        self.record_type_entry = tk.Entry(root)
        self.record_type_entry.grid(row=0, column=1)

        self.record_data_label = tk.Label(root, text="Record Data (JSON):")
        self.record_data_label.grid(row=1, column=0)
        self.record_data_entry = tk.Entry(root)
        self.record_data_entry.grid(row=1, column=1)

        self.add_button = tk.Button(root, text="Add Record", command=self.add_record)
        self.add_button.grid(row=2, column=0, columnspan=2)

        self.records_listbox = tk.Listbox(root)
        self.records_listbox.grid(row=3, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Record", command=self.delete_record)
        self.delete_button.grid(row=4, column=0, columnspan=2)

        self.records_id_array = []
        
        self.load_records()
        print(self.record_manager.records)
        print(self.records_id_array)

    def load_records(self):
        self.records_listbox.delete(0, tk.END)
        self.records_id_array = []
        for record_type in self.record_manager.RECORD_TYPES:
            for record in self.record_manager.records[record_type]:
                self.records_id_array.append(record_type + ':' + record['id'])
                self.records_listbox.insert(tk.END, f"{record_type}: {record}")

    def add_record(self):
        record_type = self.record_type_entry.get()
        record_data = self.record_data_entry.get()

        if record_type not in self.record_manager.RECORD_TYPES:
            messagebox.showerror("Error", f"Record type '{record_type}' is not supported.")
            return

        try:
            record = json.loads(record_data)
            self.record_manager.add_records(record_type, [record])
            self.load_records()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON data.")

    def delete_record(self):
        selected = self.records_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No record selected.")
            return
        
        print(selected)
        
        selected_index = selected[0]
        
        print(selected_index)
        print(self.records_id_array)
        
        # record type and record id are separated by a colon in the records_id_array
        record_type, record_id = self.records_id_array[selected_index].split(":", 1)
        
        self.record_manager.delete_records(record_type, record_id)
        self.load_records()

if __name__ == "__main__":
    root = tk.Tk()
    app = RecordManagerGUI(root)
    root.mainloop()