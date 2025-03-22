""" 
Search Bar Component

Reusable search bar component that can be used in
various parts of the application to search for data.

Version: 1.0
Last Updated: 16 Mar 2025

"""
import customtkinter as ctk

class Search(ctk.CTkFrame):
    """Search Bar Component"""
    def __init__(self, parent, search_placeholder="Search...", search_callback=None):
        super().__init__(parent, fg_color="transparent")

        self.search_callback = search_callback
        self.create_search_bar(search_placeholder)

    def create_search_bar(self, placeholder_text):
        """Create the search bar with its components"""
        # Search icon and label
        search_label = ctk.CTkLabel(
            self,
            text="Search",
            font=("Arial", 14)
        )
        search_label.pack(side="left", padx=(0, 5))

        # Search entry
        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder_text,
            height=32,
            width=300,
            fg_color="white",
            border_color="#565B5E",
            text_color="black"
        )
        self.search_entry.pack(side="left")

        # Bind the search entry to search function
        self.search_entry.bind('<KeyRelease>', self._on_search)

        # Clear search button
        self.clear_button = ctk.CTkButton(
            self,
            text="Clear",
            width=70,
            height=32,
            command=self.clear_search
        )
        self.clear_button.pack(side="left", padx=(10, 0))

    def _on_search(self, event=None):
        """Internal search handler"""
        if self.search_callback:
            self.search_callback(self.search_entry.get())

    def clear_search(self):
        """Clear search field and trigger search callback"""
