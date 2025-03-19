"""
Flights Page Class
Contains the Flights Records Table as the main content.
"""
from src.gui.pages.base import BasePage
from src.gui.components.headers import PageHeader
from src.gui.components.search import Search
from src.gui.components.buttons import SingleButton
from src.gui.components.table import DataTable
from src.gui.components.utility import DateFormatter
from src.data.record_manager import RecordManager

class FlightsPage(BasePage):
    """ Flights Page Class """
    # Intitiate Base Page
    def __init__(self, parent, navigation_callback, record_manager: RecordManager):
        super().__init__(parent, navigation_callback)
        self.record_manager = record_manager

        # Initialize attributes
        self.flights = [] #Flights List
        self.table = None #Data Table

        # Create Header
        self.header = PageHeader(
            self.content_frame,
            title="Flights",
            description="Create, edit, or manage client travel details"
        )

        # Add New Flight Button
        new_flight_btn = SingleButton(
            self.header.header_right,
            text="+ New Flight",
            command=self.on_new_flight_click
        )
        new_flight_btn.pack(side="right", pady=0)

        # Initialize content
        self.fetch_flights()
        self.setup_content()

    def fetch_flights(self):
        """
        Fetch flights data
        """
        try:
            self.flights = self.record_manager.records["flight"]
        except Exception as e:
            print(f"Error fetching flights: {e}")
            self.flights = []

    def setup_content(self):
        """Setup the main content of the flights page"""
        try:
            # Add Search Bar
            self.search_frame = Search(
                self.content_frame,
                search_placeholder="Search by Client Name",
                search_callback=self.handle_search
            )
            self.search_frame.pack(fill="x", padx=20, pady=(20, 5))

            # Create and populate table
            self.create_flight_table()

        except Exception as e:
            print(f"Error setting up content: {e}")

    def create_flight_table(self):
        """Create the flights table"""
        # Define columns
        columns = [
            {"id": "id", "text": "ID", "width": 100},
            {"id": "client", "text": "Client", "width": 150},
            {"id": "airline", "text": "Airline", "width": 150},
            {"id": "departure", "text": "From", "width": 150},
            {"id": "destination", "text": "To", "width": 150},
            {"id": "depart_date", "text": "Depart On", "width": 120},
            {"id": "return_date", "text": "Return On", "width": 120},
            {"id": "created_at", "text": "Created On", "width": 120},
        ]

        # Create table
        self.table = DataTable(
            parent=self.content_frame,
            columns=columns,
            data=self.format_flight_data(),  # Initial data
            on_row_click=self.handle_click,
            on_double_click=self.on_row_double_click,
            sort_columns=["id", "client", "airline", "departure", "destination", "depart_date", "return_date", "created_at"],
            # Pass callback in action_column
            action_column={"id": "action", "text": "Action", "callback": self.on_edit_click}
        )

        # Initial population
        self.populate_table()

    def format_flight_data(self, flights=None):
        """Format flight data for table"""
        flights_to_format = flights if flights is not None else self.flights
        return [{
            "id": flight["id"],
            "client": flight["client"],
            "airline": flight["airline"],
            "departure": flight["departure"],
            "destination": flight["destination"],
            "depart_date": DateFormatter.to_display_format(flight["depart_date"]),
            "return_date": DateFormatter.to_display_format(flight["return_date"]),
            "created_at": DateFormatter.to_display_format(flight["created_at"]),
            "action": "Edit"
        } for flight in flights_to_format]

    def populate_table(self, filtered_data=None):
        """Populate table with flight data"""
        formatted_data = self.format_flight_data(filtered_data)
        self.table.populate(formatted_data)

    def handle_search(self, search_text):
        """Handle search callback from SearchFrame"""
        search_text = search_text.lower()

        if not search_text:
            # If search is empty, show all flights
            self.populate_table()
            return

        # Filter flights based on search text
        matched_flights = [
            flight for flight in self.flights
            if search_text in flight["client"].lower()
        ]

        if matched_flights:
            self.populate_table(matched_flights)
        else:
            # Show no results found
            self.table.populate([{
                "id": "",
                "client": "No results found",
                "airline": "",
                "departure": "",
                "destination": "",
                "depart_date": "",
                "return_date": "",
                "created_at": "",
                "action": ""
            }])

    def refresh_flights(self):
        """Refresh the flights table"""
        self.fetch_flights()
        self.populate_table()

    def on_new_flight_click(self):
        """Handle new flight button click"""
        self.navigation_callback("add_new_flight")

    def on_edit_click(self, flight):
        """Handle edit action"""
        self.navigation_callback({
            "route": "edit_flight",
            "data": flight
        })

    def on_row_double_click(self, event):
        """Handle double-click on any row"""
        item = self.table.tree.identify('item', event.x, event.y)
        if item:
            values = self.table.tree.item(item)['values']
            if values:
                flight = next(
                    (f for f in self.flights if str(
                        f["id"]) == str(values[0])),
                    None
                )
                if flight:
                    self.navigation_callback({
                        "route": "edit_flight",
                        "data": flight
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
                    flight = next(
                        (f for f in self.flights if str(
                            f["id"]) == str(values[0])),
                        None
                    )
                    if flight:
                        self.navigation_callback({
                            "route": "edit_flight",
                            "data": flight
                        })
