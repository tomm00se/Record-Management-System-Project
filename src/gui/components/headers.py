"""Header Component Module"""
import customtkinter as ctk

class PageHeader(ctk.CTkFrame):
    """Page Header Component"""
    def __init__(self, parent, title, description=None):
        super().__init__(parent, fg_color="transparent", corner_radius=0)
        self.pack(fill="x", padx=20, pady=(20, 0))

        # Create left side container
        self.header_left = ctk.CTkFrame(self, fg_color="transparent")
        self.header_left.pack(side="left", fill="x", expand=True)

        # Create right side container
        self.header_right = ctk.CTkFrame(self, fg_color="transparent")
        self.header_right.pack(side="right", pady=5)

        # Title
        self.title_label = ctk.CTkLabel(
            self.header_left,
            text=title,
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(anchor="w", pady=0)

        # Description
        if description:
            self.desc_label = ctk.CTkLabel(
                self.header_left,
                text=description,
                font=("Arial", 13)
            )
            self.desc_label.pack(anchor="w", pady=(0, 5))


class FormHeader(ctk.CTkFrame):
    """Form Header Component"""

    def __init__(self, parent, title, description=None):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="x", padx=20, pady=(20, 10))

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Arial Bold", 24)
        )
        self.title_label.pack(anchor="w")

        # Description
        if description:
            self.desc_label = ctk.CTkLabel(
                self,
                text=description,
                font=("Arial", 13)
            )
            self.desc_label.pack(anchor="w", pady=(0, 5))
