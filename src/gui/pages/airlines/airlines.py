"""
Airlines Page Class
Contains the Airlines Records Table as the main content.
"""
from src.gui.pages.base import BasePage
from src.gui.components.headers import PageHeader
from src.gui.components.search import Search
from src.gui.components.buttons import SingleButton
from src.gui.components.table import DataTable
from src.gui.components.utility import DateFormatter
from src.data.record_manager import RecordManager

class AirlinesPage(BasePage):
    """ Airlines Page Class """

    def __init__(self, parent, navigation_callback, record_manager: RecordManager):
        super().__init__(parent, navigation_callback)  # Initialize the base page first
        self.record_manager = record_manager

        # Initialize attributes
        self.airlines = []  # Airlines List
        self.table = None  # Data Table

        # Create page header using base method
        self.header = PageHeader(
            self.content_frame,
            title="Airlines",
            description="Create, edit, or manage airline companies"
        )

        # Add New Airline Button
        new_airline_btn = SingleButton(
            self.header.header_right,
            text="+ New Airline",
            command=self.on_new_airline_click
        )
        new_airline_btn.pack(side="right", pady=0)

        # Initialize content
        self.fetch_airlines()
        self.setup_content()

    def fetch_airlines(self):
        """
        Fetch airlines data
        """
        try:
            self.airlines = self.record_manager.records["airline"]
        except Exception as e:
            print(f"Error fetching airlines: {e}")
            self.airlines = []

    def setup_content(self):
        """Setup the main content of the airlines page"""
        try:
            # Add this to see the actual data structure
            print("Load Airlines Data:", self.airlines)
            # Add Search Bar
            self.search_frame = Search(
                self.content_frame,
                search_placeholder="Search by Airline Name",
                search_callback=self.handle_search
            )
            self.search_frame.pack(fill="x", padx=20, pady=(20, 5))

            # Create Table
            self.create_airline_table()

        except Exception as e:
            print(f"Error setting up content: {e}")

    def create_airline_table(self):
        """Create the airline table"""
        # Define columns
        columns = [
            {"id": "id", "text": "ID", "width": 100},
            {"id": "company_name", "text": "Airline", "width": 150},
            {"id": "country", "text": "Country", "width": 150},
            {"id": "created_at", "text": "Created On", "width": 150},
        ]

        # Create table
        self.table = DataTable(
            parent=self.content_frame,
            columns=columns,
            data=self.format_airline_data(),  # Initial data
            on_row_click=self.handle_click,
            on_double_click=self.on_row_double_click,
            sort_columns=["id", "company_name", "country", "created_at"],
            # Pass callback in action_column
            action_column={"id": "action", "text": "Action", "callback": self.on_edit_click}
        )

        # Initial population
        self.populate_table()

    def format_airline_data(self, airlines=None):
        """Format airline data for table"""
        airlines_to_format = airlines if airlines is not None else self.airlines
        return [{
            "id": airline["id"],
            "company_name": airline["company_name"],
            "country": airline["country"],
            "created_at": DateFormatter.to_display_format(airline["created_at"]),
            "action": "Edit"
        } for airline in airlines_to_format]

    def populate_table(self, filtered_data=None):
        """Populate table with airline data"""
        formatted_data = self.format_airline_data(filtered_data)
        self.table.populate(formatted_data)

    def handle_search(self, search_text):
        """Handle search callback from SearchFrame"""
        search_text = search_text.lower()

        if not search_text:
            # If search is empty, show all airlines
            self.populate_table()
            return

        # Filter airlines based on search text
        matched_airlines = [
            airline for airline in self.airlines
            if search_text in airline["company_name"].lower()
        ]

        if matched_airlines:
            self.populate_table(matched_airlines)
        else:
            # Show no results found
            self.table.populate([{
                "id": "",
                "company_name": "No results found",
                "country": "",
                "created_at": "",
                "action": ""
            }])

    def refresh_airlines(self):
        """Refresh the airlines table"""
        self.fetch_airlines()
        self.populate_table()

    def on_new_airline_click(self):
        """Handle new airline button click"""
        self.navigation_callback("add_new_airline")

    def on_edit_click(self, airline):
        """Handle edit action"""
        self.navigation_callback({
            "route": "edit_airline",
            "data": airline
        })

    def on_row_double_click(self, event):
        """Handle double-click on any row"""
        item = self.table.tree.identify('item', event.x, event.y)
        if item:
            values = self.table.tree.item(item)['values']
            if values:
                airline = next(
                    (f for f in self.airlines if str(
                        f["id"]) == str(values[0])),
                    None
                )
                if airline:
                    self.navigation_callback({
                        "route": "edit_airline",
                        "data": airline
                    })

    def handle_click(self, event):
        """Handle click events on the table"""
        region = self.table.tree.identify("region", event.x, event.y)
        if region == "cell":
            column = self.table.tree.identify_column(event.x)
            item = self.table.tree.identify_row(event.y)

            # Check if click is in action column (last column)
            if column == f"#{len(self.table.columns) + 1}":
                values = self.table.tree.item(item)['values']
                if values:
                    airline = next(
                        (f for f in self.airlines if str(
                            f["id"]) == str(values[0])),
                        None
                    )
                    if airline:
                        self.navigation_callback({
                            "route": "edit_airline",
                            "data": airline
                        })
