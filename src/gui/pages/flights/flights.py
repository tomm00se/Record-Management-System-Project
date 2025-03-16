"""
Flights Page Class

Contains the Flights Records Table as the main content.
"""
from tkinter import ttk
import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.gui.components.search import Search
from src.gui.components.utility import DateFormatter

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

    def fetch_flights(self):
        """
        Fetch flights data from your data source
        For now, using sample data
        """
        try:
            # This is sample data - replace with your actual data fetching logic
            self.flights = [
                {
                    "id": "F0001",
                    "type": "Flight",
                    "client": "Leona Wong",
                    "airline": "Cathay Pacific Airways",
                    "departure": "Hong Kong",
                    "destination": "London",
                    "depart_date": "10 Apr 2025",
                    "created_date": "2024-03-15T10:30:00Z"
                },
                {
                    "id": "F0002",
                    "type": "Flight",
                    "client": "Leona Wong",
                    "airline": "Cathay Pacific Airways",
                    "departure": "London",
                    "destination": "Hong Kong",
                    "depart_date": "30 Apr 2025",
                    "created_date": "2024-03-15T10:30:00Z"
                },
                {
                    "id": "F0003",
                    "type": "Flight",
                    "client": "Tommy Bowden",
                    "airline": "British Airways",
                    "departure": "London",
                    "destination": "Hong Kong",
                    "depart_date": "28 Apr 2025",
                    "created_date": "2024-03-16T10:30:00Z"
                }
            ]
        except Exception as e:
            print(f"Error fetching flights: {e}")
            self.flights = []

    def setup_content(self):
        """Setup the main content of the flights page"""
        try:
            # Add New Flight Button
            self.create_action_buttons()

            # Add Search Bar
            self.search_frame = Search(
                self.content_frame,
                search_placeholder="Search by Client Name",
                search_callback=self.handle_search
            )
            self.search_frame.pack(fill="x", padx=10, pady=(0, 10))

            # Create Table
            self.create_flight_table()

            # Populate the table with data
            self.populate_table()

        except Exception as e:
            print(f"Error setting up content: {e}")

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
            show="headings",
            selectmode="browse"  # Single selection mode
        )

        # Configure column headings and widths
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Action":
                self.tree.column(col, width=100, anchor="center")
            else:
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

        # Bind double-click event
        self.tree.bind('<Double-1>', self.on_row_double_click)

        #Bind click event for the Action column
        self.tree.bind('<Button-1>', self.handle_click)

    def populate_table(self):
        """Populate table with flight data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add data to table
        for flight in self.flights:
            formatted_created_date = DateFormatter.to_display_format(
                flight["created_date"])

            # Insert row with values
            item_id = self.tree.insert("", "end", values=(
                flight["id"],
                flight["client"],
                flight["airline"],
                flight["departure"],
                flight["destination"],
                flight["depart_date"],
                formatted_created_date,
                "Edit"  # Using edit symbol instead of button
            ))

           # Bind click event for the Action column
            self.tree.tag_bind(item_id, 'edit_action',
                               lambda e, f=flight: self.on_edit_click(f))

    def handle_search(self, search_text):
        """Handle search callback from SearchFrame"""
        search_text = search_text.lower()

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filter and display matching flights
        matched_flights = [
            flight for flight in self.flights
            if search_text in flight["client"].lower()
        ]

        if matched_flights:
            for flight in matched_flights:
                formatted_created_date = DateFormatter.to_display_format(
                    flight["created_date"])

                # Insert row
                item_id = self.tree.insert("", "end", values=(
                    flight["id"],
                    flight["client"],
                    flight["airline"],
                    flight["departure"],
                    flight["destination"],
                    flight["depart_date"],
                    formatted_created_date,
                    "Edit"  # Simple text for edit action
                ))

                # Place button in the last column
                self.tree.tag_bind(item_id, 'edit_action',
                                   lambda e, f=flight: self.on_edit_click(f))
        else:
            self.show_no_results()

    # Helper Methods
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

    def refresh_flights(self):
        """Refresh the flights table"""
        self.fetch_flights()
        self.populate_table()

    # Button Actions
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

    def on_new_flight_click(self):
        """Handle new flight button click"""
        self.navigation_callback("add_new_flight")

    def on_edit_click(self, flight):
        """Handle edit action"""
        print(f"Editing flight: {flight['id']}")  # Debug print
        # Pass the flight data as part of the route data
        self.navigation_callback({
            "route": "edit_flight",
            "data": flight
    })

    def on_row_double_click(self, event):
        """Handle double-click on any row"""
        item = self.tree.identify('item', event.x, event.y)
        if item:
            values = self.tree.item(item)['values']
            if values:
                flight = next(
                    (f for f in self.flights if f["id"] == values[0]),
                    None
                )
                if flight:
                    self.navigation_callback({
                        "route": "edit_flight",
                        "data": flight
                    })


    def handle_click(self, event):
        """Handle click events on the table"""
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            column = self.tree.identify_column(event.x)
            item = self.tree.identify_row(event.y)

        if region == "cell":
            column = self.tree.identify_column(event.x)
            item = self.tree.identify_row(event.y)

            if column == "#8":  # Action column
                values = self.tree.item(item)['values']
                if values:
                    flight = next(
                        (f for f in self.flights if f["id"] == values[0]),
                        None
                    )
                    if flight:
                        print("DEBUG: Double-click on flight:",
                              flight)  # Debug print
                        self.navigation_callback({
                            "route": "edit_flight",
                            "data": flight
                        })
