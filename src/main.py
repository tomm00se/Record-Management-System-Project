import tkinter as tk
from gui.record_gui import RecordManagerGUI

def main():
    root = tk.Tk()
    app = RecordManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()