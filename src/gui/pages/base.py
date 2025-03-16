"""
Base Page Class

This module provides a base template for all pages in the application.
Contains common functionality and settings that all pages will inherit.
"""
import customtkinter as ctk
# from PIL import Image
# from .components.sidebar import Sidebar


class BasePage(ctk.CTkFrame):
    """
    Base page class that all pages will inherit from
    """
    def __init__(self, parent, navigation_callback):
        super().__init__(parent)
        self.parent = parent
        self.navigation_callback = navigation_callback
        # Make the base page fill its parent
        self.pack(fill="both", expand=True)

        # Initialize the Header Frame
        self.header_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",  # Background color
            corner_radius=0    # No rounded corners
        )
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))

        # Initialize the Content Frame
        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",  # Background color
            corner_radius=0    # No rounded corners
        )
        self.content_frame.pack(fill="both", expand=True)

    def show_loading(self):
        """Show loading indicator"""
        self.loading_label = ctk.CTkLabel(
            self,
            text="Loading...",
            font=("Arial", 14)
        )
        self.loading_label.place(relx=0.5, rely=0.5, anchor="center")

    def hide_loading(self):
        """Hide loading indicator"""
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()

    def clear_page(self):
        """Clear all widgets from the page"""
        for widget in self.winfo_children():
            widget.pack_forget()

    def show_error(self, message):
        """Show error message"""
        error_label = ctk.CTkLabel(
            self,
            text=message,
            text_color="red",
            font=("Arial", 13)
        )
        error_label.pack(pady=10)

    def create_header(self, title, description=None):
        """Create Standard Page Header"""
        title_label = ctk.CTkLabel(
            self.header_frame,
            text=title,
            font=("Arial", 24, "bold")
        )
        title_label.pack(side="left")

        if description:
            desc_label = ctk.CTkLabel(
                self.header_frame,
                text=description,
                font=("Arial", 13)
            )
            desc_label.pack(side="bottom", padx=(20, 0))
