"""
Reusable Button Components
"""
from tkinter import messagebox
import customtkinter as ctk


class FormButtons(ctk.CTkFrame):
    """ 
    Form Buttons Components
    """

    def __init__(
        self,
        parent,
        cancel_command=None,
        save_command=None,
        save_text="Save",
        cancel_text="Cancel",
        **kwargs
    ):
        super().__init__(parent, fg_color="transparent", **kwargs)

        # Common Button Styles
        button_style = {
            "height": 30,
            "width": 108,
            "corner_radius": 3
        }

        # Create a container for right alignment
        button_container = ctk.CTkFrame(self, fg_color="transparent")
        button_container.pack(side="right")

        # Cancel Button
        self.cancel_btn = ctk.CTkButton(
            button_container,
            text=cancel_text,
            fg_color="#d1d1d6",
            hover_color="#c7c7CC",
            text_color="#444444",
            command=cancel_command,
            **button_style
        )
        self.cancel_btn.pack(side="left", padx=(0, 10))

        # Save Button
        self.save_btn = ctk.CTkButton(
            button_container,
            text=save_text,
            fg_color="#007aff",
            hover_color="#006be0",
            text_color="#ffffff",
            command=save_command,
            **button_style
        )
        self.save_btn.pack(side="left")

    def disable_buttons(self):
        """Disable states"""
        self.cancel_btn.configure(state="disabled")
        self.save_btn.configure(state="disabled")

    def enable_buttons(self):
        """Enable states"""
        self.cancel_btn.configure(state="normal")
        self.save_btn.configure(state="normal")


class DeleteButton(ctk.CTkFrame):
    """ 
    Delete Button
    """

    def __init__(
        self,
        parent,
        delete_command=None,
        delete_text="Delete",
        confirm_message="Are you sure you want to delete this record?",
        **kwargs
    ):
        super().__init__(parent, fg_color="transparent", **kwargs)

        self.delete_command = delete_command
        self.confirm_message = confirm_message

        # Delete Button
        self.delete_btn = ctk.CTkButton(
            parent,
            text=delete_text,
            command=self.confirm_delete,
            fg_color="#606060",
            hover_color="#515151",
            text_color="#ffffff",
            height=30,
            width=108,
            corner_radius=3
        )
        self.delete_btn.pack(side="right", padx=0)

    def confirm_delete(self):
        """Show confirmation dialog before deletion"""
        if messagebox.askyesno("Confirm Delete", self.confirm_message):
            if self.delete_command:
                self.delete_command()

    def disable_button(self):
        """Disable state"""
        self.delete_btn.configure(state="disabled")

    def enable_button(self):
        """Enable state"""
        self.delete_btn.configure(state="normal")


class SingleButton(ctk.CTkButton):
    """ 
    Single Button
    """

    def __init__(
        self,
        parent,
        text,
        command,
        **kwargs
    ):
        super().__init__(
            parent,
            text=text,
            command=command,
            fg_color="#007aff",
            hover_color="#006be0",
            text_color="#ffffff",
            height=30,
            width=108,
            corner_radius=3,
            **kwargs
        )
