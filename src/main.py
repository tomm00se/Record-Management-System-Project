"""Record Management System GUI Application"""
import tkinter as tk
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from src.gui.record_gui import RecordMgmtSystem

def main():
    """Create and start application"""
    root = tk.Tk()
    app = RecordMgmtSystem(root)
    app.run()


if __name__ == "__main__":
    main()
