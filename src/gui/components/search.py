""" 
Search Bar Component

Reusable search bar component that can be used in
various parts of the application to search for data.

Version: 1.0
Last Updated: 16 Mar 2025

"""
import customtkinter as ctk
from src.gui.components.buttons import SingleButton

class Search(ctk.CTkFrame):
    """Search Bar Component"""
    def __init__(self, parent, search_placeholder="Search...", search_callback=None):
        super().__init__(parent, fg_color="transparent", height=40)

        # Make the frame expand horizontally
        self.pack_propagate(False)  # Prevent frame from shrinking

        self.search_callback = search_callback
        self.create_search_bar(search_placeholder)

    def create_search_bar(self, placeholder_text):
        """Create the search bar with its components"""
        # Container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)

        # Left frame for search entry
        search_frame = ctk.CTkFrame(container, fg_color="transparent")
        search_frame.pack(side="left", fill="x", expand=True)

        # Search entry
        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text=placeholder_text,
            height=32,
            fg_color="white",
            border_color="#dfe4ea",
            text_color="black"
        )
        self.search_entry.pack(side="left", fill="x", expand=True)

        # Bind the search entry to search function
        self.search_entry.bind('<KeyRelease>', self._on_search)

        # Right frame for button
        button_frame = ctk.CTkFrame(container, fg_color="transparent")
        button_frame.pack(side="right", padx=(10, 0))

        # Clear search button
        self.clear_button = SingleButton(
            parent=button_frame,
            text="Clear",
            command=self.clear_search
        )
        self.clear_button.pack(side="right")

    def _on_search(self, event=None):
        """Internal search handler"""
        if self.search_callback:
            self.search_callback(self.search_entry.get())

    def clear_search(self):
        """Clear search field and trigger search callback"""
        self.search_entry.delete(0, 'end')
        if self.search_callback:
            self.search_callback("")
