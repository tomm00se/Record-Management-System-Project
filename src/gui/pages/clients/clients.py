"""
Clients Page Class

Contains the Clients Records Table as the main content.
"""
from tkinter import ttk
import customtkinter as ctk
from src.gui.components.utility import DateFormatter
from src.gui.pages.base import BasePage
from src.data.record_manager import RecordManager
from src.gui.components.search import Search


class ClientsPage(BasePage):
    """ Clients Page Class """

    def __init__(self, parent, navigation_callback, record_manager: RecordManager):
        super().__init__(parent, navigation_callback)  # Initialize the base page first
        
        self.record_manager = record_manager

        # Initialize attributes first
        self.clients = []  # Initialize clients list
        self.tree = None   # Initialize tree

        # Create page header using base method
        self.create_header(
            title="Clients",
            description="Create, edit, or manage client records"
        )

        # Fetch data before creating content
        self.fetch_clients()

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
        """Setup the main content of the clients page"""
        try:
            # Add New Client Button
            self.create_action_buttons()
            
            # Add Search Bar
            self.search_frame = Search(
                self.content_frame,
                search_placeholder="Search by Client Name",
                search_callback=self.handle_search
            )
            self.search_frame.pack(fill="x", padx=10, pady=(0, 10))


            # Create Table
            self.create_client_table()
        except Exception as e:
            print(f"Error setting up content: {e}")

    def create_action_buttons(self):
        """Create action button to add new client"""
        button_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color="transparent"
        )
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        new_client_btn = ctk.CTkButton(
            button_frame,
            text="+ New Client",
            command=self.on_new_client_click
        )
        new_client_btn.pack(side="right")

    def create_client_table(self):
        """Create the clients table"""
        # Create a frame to hold both table and scrollbar
        table_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        table_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # Table Columns
        columns = ("ID", "Name", "City", "Country", "Phone",
                   "Email", "Created On", "Action")

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
        
        # Bind double-click event
        self.tree.bind('<Double-1>', self.on_row_double_click)

        #Bind click event for the Action column
        self.tree.bind('<Button-1>', self.handle_click)

        # Insert the sample data
        self.populate_table()

    def populate_table(self):
        """Populate table with client data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add data to table
        for client in self.clients:
            formatted_created_at = DateFormatter.to_display_format(
                client["created_at"])
            self.tree.insert("", "end", values=(
                client["id"],
                client["name"],
                client["city"],
                client["country"],
                client["phone"],
                client["email"],
                formatted_created_at,
                "Edit"
            ))
    
    def handle_search(self, search_text):
        """Handle search callback from SearchFrame"""
        search_text = search_text.lower()

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Filter and display matching flights
        matched_clients = [
            client for client in self.clients
            if search_text in client["name"].lower()
        ]

        if matched_clients:
            for client in matched_clients:
                formatted_created_at = DateFormatter.to_display_format(
                    client["created_at"])

                # Insert row
                item_id = self.tree.insert("", "end", values=(
                    client["id"],
                    client["name"],
                    client["city"],
                    client["country"],
                    client["phone"],
                    client["email"],
                    formatted_created_at,
                    "Edit"
                ))

                # Place button in the last column
                self.tree.tag_bind(item_id, 'edit_action',
                                   lambda e, f=client: self.on_edit_click(f))
        else:
            # Show no results found
            self.tree.insert("", "end", values=(
                "",
                "No results found",
            ))

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

    def refresh_clients(self):
        """Refresh the clients table"""
        self.fetch_clients()
        self.populate_table()

    def on_new_client_click(self):
        """Handle new client button click"""
        self.navigation_callback("add_new_client")
        
    def on_edit_click(self, client):
        """Handle edit action"""
        print(f"Editing client: {client['id']}")  # Debug print
        # Pass the client data as part of the route data
        self.navigation_callback({
            "route": "edit_client",
            "data": client
    })

    def on_row_double_click(self, event):
        """Handle double-click on any row"""
        item = self.tree.identify('item', event.x, event.y)
        if item:
            values = self.tree.item(item)['values']
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
                    client = next(
                        (f for f in self.clients if f["id"] == values[0]),
                        None
                    )
                    if client:
                        print("DEBUG: Double-click on client:",
                              client)  # Debug print
                        self.navigation_callback({
                            "route": "edit_client",
                            "data": client
                        })
