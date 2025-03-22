"""
Reusable Data Table
A reusable data table component for displaying tabular data in the application
"""
from tkinter import ttk
import customtkinter as ctk

class DataTable:
    """
    DataTable Class
    """
    def __init__(
        self,
        parent,
        columns,
        data=None,
        on_row_click=None,
        on_double_click=None,
        sort_columns=None,
        action_column=None,
        numeric_columns=None
    ):
        """
        Initialize DataTable
        """
        self.parent = parent
        self.columns = columns
        self.data = data or []
        self.on_row_click = on_row_click
        self.on_double_click = on_double_click
        self.sort_columns = sort_columns or []
        self.action_column = action_column
        self.numeric_columns = numeric_columns or ["id"]  # Default numeric columns
        self.action_callback = action_column.get('callback') if action_column else None
        self.setup_table()

    def setup_table(self):
        """Setup the table widget and its styling"""
        # Create table frame
        self.frame = ctk.CTkFrame(
            self.parent,
            fg_color="#ffffff",
            corner_radius=10
        )
        self.frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Style configuration
        self.setup_style()

        # Create Treeview
        column_ids = [col["id"] for col in self.columns]
        if self.action_column:
            column_ids.append(self.action_column["id"])

        self.tree = ttk.Treeview(
            self.frame,
            columns=column_ids,
            show="headings",
            selectmode="browse"
        )

        # Configure columns
        self.setup_columns()

        # Add sorting if enabled
        if self.sort_columns:
            self.setup_sorting()

        # Pack the tree
        self.tree.pack(fill="both", expand=True, padx=0, pady=0)

        # Bind events
        self.setup_bindings()
        
    def setup_style(self):
        """Configure the table styling"""
        style = ttk.Style()
        style.configure(
            "Treeview",
            background="white",
            rowheight=20,
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading",
            background="white",
            foreground="#444444",
            font=("Arial", 12, "normal"),
            relief="flat"
        )

    def setup_columns(self):
        """Configure table columns"""
        for col in self.columns:
            self.tree.heading(col["id"], text=col["text"])
            self.tree.column(
                col["id"],
                width=col.get("width", 150),
                anchor=col.get("anchor", "w"),
                stretch=col.get("stretch", True)
            )

        if self.action_column:
            self.tree.heading(
                self.action_column["id"], text=self.action_column["text"])
            self.tree.column(
                self.action_column["id"],
                width=100,
                anchor="center",
                stretch=False
            )

    def setup_sorting(self):
        """Setup column sorting functionality"""
        def sort_column(treeView, col, reverse):
            list = [(treeView.set(k, col), k) for k in treeView.get_children('')] # L is a list

            try:
                # Handle numeric sorting
                if col in self.numeric_columns:
                    list.sort(key=lambda t: float(
                        t[0]) if t[0] else 0, reverse=reverse)
                else:
                    list.sort(reverse=reverse)
            except ValueError:
                list.sort(reverse=reverse)

            # Rearrange items
            for index, (_, k) in enumerate(list):
                treeView.move(k, '', index)

            # Update column headers with sort indicators
            for column in self.sort_columns:
                if column != self.action_column["id"]:
                    # Get original column text
                    original_text = next(
                        (col_def["text"] for col_def in self.columns
                         if col_def["id"] == column),
                        column
                    )

                    # Add sort indicator if this is the sorted column
                    if column == col:
                        indicator = " ↑" if reverse else " ↓"
                    else:
                        indicator = ""

                    treeView.heading(column, text=original_text + indicator)

            # Update click handler
            treeView.heading(
                col,
                command=lambda c=col: sort_column(treeView, c, not reverse)
            )

        # Initialize sorting for sortable columns
        for col in self.sort_columns:
            if col != self.action_column["id"]:
                self.tree.heading(
                    col,
                    command=lambda c=col: sort_column(self.tree, c, False)
                )

    def setup_bindings(self):
        """Setup event bindings"""
        if self.on_double_click:
            self.tree.bind('<Double-1>', self.on_double_click)
        if self.on_row_click:
            self.tree.bind('<Button-1>', self.on_row_click)

    def populate(self, data=None):
        """Populate table with data"""
        if data is not None:
            self.data = data

        self.tree.delete(*self.tree.get_children())

        for item in self.data:
            values = [item.get(col["id"], "") for col in self.columns]
            if self.action_column:
                values.append(item.get(self.action_column["id"], "Edit"))
            self.tree.insert("", "end", values=values)

    def clear(self):
        """Clear all data from table"""
        self.tree.delete(*self.tree.get_children())
