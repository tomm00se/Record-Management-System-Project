import tkinter as tk
from gui.record_gui3 import RecordMgmtSystem

def main():
    root = tk.Tk()
    app = RecordMgmtSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()