"""
Base Page Class

This module provides a base template for all pages in the application.
Contains common functionality and settings that all pages will inherit.
"""
import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    """
    Base page class that all pages will inherit from
    """

    def __init__(self, parent, navigation_callback):
        super().__init__(parent, fg_color="#ececec")
        self.parent = parent
        self.navigation_callback = navigation_callback
        # Make the base page fill its parent
        self.pack(fill="both", expand=True)

        # Initialize the Content Frame
        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        self.content_frame.pack(fill="both", expand=True, pady=0)

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
