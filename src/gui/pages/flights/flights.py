"""
Flights Page Class

Contains the Flights Records Table as the main content.
"""
from tkinter import ttk
import customtkinter as ctk
from ..base import BasePage


class FlightsPage(BasePage):
    """ Flights Page Class """

    def __init__(self, parent, navigation_callback):
        super().__init__(parent, navigation_callback)  # Initialize the base page first

        # Initialize attributes first
        self.flights = []  # Initialize flights list
        self.tree = None   # Initialize tree

        # Create page header using base method
        self.create_header(
            title="Flights",
            description="Create, edit, or manage client travel details"
        )

        # Fetch data before creating content
        self.fetch_flights()

        # Create main content
        self.setup_content()

    def show_loading(self):
        """Show loading indicator"""
        self.loading_label = ctk.CTkLabel(
            self.content_frame,
            text="Loading...",
            font=("Arial", 14)
        )
        self.loading_label.pack(pady=20)

    def hide_loading(self):
        """Hide loading indicator"""
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()

    def setup_content(self):
        """Setup the main content of the flights page"""
        try:
            # Add New Flight Button
            self.create_action_buttons()

            # Create Table
            self.create_flight_table()
        except Exception as e:
            print(f"Error setting up content: {e}")

    def create_action_buttons(self):
        """Create action buttons like 'New Flight'"""
        button_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        new_flight_btn = ctk.CTkButton(
            button_frame,
            text="+ New Flight",
            command=self.on_new_flight_click
        )
        new_flight_btn.pack(side="right")

    def create_flight_table(self):
        """Create the flights table"""
        # Create a frame to hold both table and scrollbar
        table_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # Table Columns
        columns = ("ID", "Client", "Airline", "From", "To",
                   "Depart On", "Created On", "Action")

        # Initialize and configure Treeview
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        # Configure column headings and widths
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Create scrollbar first
        scrollbar = ttk.Scrollbar(
            self.content_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Pack scrollbar and tree
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Insert the sample data
        self.populate_table()

    def populate_table(self):
        """Populate table with flight data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add data to table
        for flight in self.flights:
            self.tree.insert("", "end", values=(
                flight["id"],
                flight["client"],
                flight["airline"],
                flight["departure"],
                flight["destination"],
                flight["depart_date"],
                flight["created_date"]
            ))

    def fetch_flights(self):
        """
        Fetch flights data from your data source
        For now, using sample data
        """
        try:
            # This is sample data - replace with your actual data fetching logic
            self.flights = [
                {
                    "id": "0001",
                    "client": "Leona Wong",
                    "airline": "Cathay Pacific Airways",
                    "departure": "Hong Kong",
                    "destination": "London",
                    "depart_date": "10 Apr 2025",
                    "created_date": "09 Mar 2025 18:38"
                },
                {
                    "id": "0002",
                    "client": "Leona Wong",
                    "airline": "Cathay Pacific Airways",
                    "departure": "London",
                    "destination": "Hong Kong",
                    "depart_date": "30 Apr 2025",
                    "created_date": "09 Mar 2025 18:38"
                }
            ]
        except Exception as e:
            print(f"Error fetching flights: {e}")
            self.flights = []

    def refresh_flights(self):
        """Refresh the flights table"""
        self.fetch_flights()
        self.populate_table()

    def on_new_flight_click(self):
        """Handle new flight button click"""
        self.navigation_callback("addNewFlight")
