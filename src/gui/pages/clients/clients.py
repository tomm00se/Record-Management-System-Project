"""
Clients Page Class

Contains the Clients Records Table as the main content.
"""
from src.gui.pages.base import BasePage
from src.gui.components.headers import PageHeader
from src.gui.components.search import Search
from src.gui.components.buttons import SingleButton
from src.gui.components.table import DataTable
from src.gui.components.utility import DateFormatter
from src.data.record_manager import RecordManager


class ClientsPage(BasePage):
    """ Clients Page Class """
    # Intitiate Base Page

    def __init__(self, parent, navigation_callback, record_manager: RecordManager):
        super().__init__(parent, navigation_callback)
        self.record_manager = record_manager

        # Initialize attributes first
        self.clients = []  # Initialize clients list
        self.table = None  # Data Table

        # Create Header
        self.header = PageHeader(
            self.content_frame,
            title="Clients",
            description="Create, edit, or manage client records"
        )

        # Add New Client Button
        new_client_btn = SingleButton(
            self.header.header_right,
            text="+ New Client",
            command=self.on_new_client_click
        )
        new_client_btn.pack(side="right", pady=0)

        # Initialize content
        self.fetch_clients()
        self.setup_content()

    def fetch_clients(self):
        """
        Fetch clients data from your data source
        For now, using sample data
        """
        try:
            self.clients = self.record_manager.records["client"]
        except Exception as e:
            print(f"Error fetching clients: {e}")
            self.clients = []

    def setup_content(self):
        """Setup the main content of the clients page"""
        try:
            # Add Search Bar
            self.search_frame = Search(
                self.content_frame,
                search_placeholder="Search by Client Name",
                search_callback=self.handle_search
            )
            self.search_frame.pack(fill="x", padx=20, pady=(20, 5))

            # Create and populate table
            self.create_client_table()

        except Exception as e:
            print(f"Error setting up content: {e}")

    def create_client_table(self):
        """Create the clients table"""
        # Define columns
        columns = [
            {"id": "id", "text": "ID", "width": 100},
            {"id": "name", "text": "Name", "width": 150},
            {"id": "phone", "text": "Phone", "width": 150},
            {"id": "email", "text": "Email", "width": 120},
            {"id": "city", "text": "City", "width": 150},
            {"id": "country", "text": "Country", "width": 150},
            {"id": "created_at", "text": "Created On", "width": 120},
        ]

        # Create table
        self.table = DataTable(
            parent=self.content_frame,
            columns=columns,
            data=self.format_client_data(),  # Initial data
            on_row_click=self.handle_click,
            on_double_click=self.on_row_double_click,
            sort_columns=["id", "name", "city", "country",
                          "phone", "email", "created_at"],
            # Pass callback in action_column
            action_column={"id": "action", "text": "Action",
                           "callback": self.on_edit_click}
        )

        # Initial population
        self.populate_table()

    def format_client_data(self, clients=None):
        """Format client data for table"""
        clients_to_format = clients if clients is not None else self.clients
        return [{
            "id": client["id"],
            "name": client["name"],
            "city": client["city"],
            "country": client["country"],
            "phone": client["phone"],
            "email": client["email"],
            "created_at": DateFormatter.to_display_format(client["created_at"]),
            "action": "Edit"
        } for client in clients_to_format]

    def populate_table(self, filtered_data=None):
        """Populate table with client data"""
        formatted_data = self.format_client_data(filtered_data)
        self.table.populate(formatted_data)

    def handle_search(self, search_text):
        """Handle search callback from SearchFrame"""
        search_text = search_text.lower()

        if not search_text:
            # If search is empty, show all clients
            self.populate_table()
            return

        # Filter and display matching clients
        matched_clients = [
            client for client in self.clients
            if search_text in client["name"].lower()
        ]

        if matched_clients:
            self.populate_table(matched_clients)
        else:
            # Show no results found
            self.table.populate([{
                "id": "",
                "name": "No results found",
                "city": "",
                "country": "",
                "phone": "",
                "email": "",
                "created_at": "",
                "action": ""
            }])

    def refresh_clients(self):
        """Refresh the clients table"""
        self.fetch_clients()
        self.populate_table()

    def on_new_client_click(self):
        """Handle new client button click"""
        self.navigation_callback("add_new_client")

    def on_edit_click(self, client):
        """Handle edit action"""
        self.navigation_callback({
            "route": "edit_client",
            "data": client
        })

    def on_row_double_click(self, event):
        """Handle double-click on any row"""
        item = self.table.tree.identify('item', event.x, event.y)
        if item:
            values = self.table.tree.item(item)['values']
            if values:
                client = next(
                    (f for f in self.clients if f["id"] == values[0]),
                    None
                )
                if client:
                    self.navigation_callback({
                        "route": "edit_client",
                        "data": client
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
                    client = next(
                        (f for f in self.clients if str(
                            f["id"]) == str(values[0])),
                        None
                    )
                    if client:
                        self.navigation_callback({
                            "route": "edit_client",
                            "data": client
                        })
