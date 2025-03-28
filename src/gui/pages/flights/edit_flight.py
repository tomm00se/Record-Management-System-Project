""" Edit Flight Page Module """
from tkinter import messagebox
import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.gui.components.headers import FormHeader
from src.gui.components.buttons import FormButtons, DeleteButton
from src.gui.components.form import FormComponents
from src.gui.components.utility import DateFormatter
from src.data.record_manager import RecordManager


class EditFlightPage(BasePage):
    """ Edit Flight Page Class """

    def __init__(self, parent, navigation_callback, record_manager: RecordManager, flight_data=None, **kwargs):
        super().__init__(parent, navigation_callback, **kwargs)
        self.record_manager = record_manager
        self.form_components = FormComponents()

        # Store flight data
        self.flight_data = flight_data

        # Create Header
        self.header = FormHeader(
            self.content_frame,
            title="Edit Flight",
            description="Edit the travel details to update the flight record"
        )
        self.header.pack(fill="x", padx=20, pady=(20, 0))

        # Create Delete Button Container
        self.delete_container = ctk.CTkFrame(
            self.content_frame, fg_color="transparent")
        self.delete_container.pack(fill="x", padx=20, pady=0)
        # Delete Flight Button
        self.delete_button = DeleteButton(
            self.delete_container,
            delete_command=self.on_delete,
            confirm_message="Are you sure you want to delete this record?"
        )

        # Form container
        self.form_container = ctk.CTkFrame(
            self.content_frame, fg_color="transparent")
        self.form_container.pack(fill="x", padx=20, pady=0)

        # Create form
        self.create_form()

    def create_form(self):
        """Create the form for adding a new flight"""
        # Client Selection
        self.client = self.form_components.create_form_row(
            self.form_container,
            "Client",
            required=True,
            field_type="option",
            values=self.get_clients()
        )
        self.client.pack(fill="x", pady=(0, 0))
        self.client.set(self.flight_data["client"])

        # Airline Selection
        self.airline = self.form_components.create_form_row(
            self.form_container,
            "Airline",
            required=True,
            field_type="option",
            values=self.get_airlines()
        )
        self.airline.pack(fill="x", pady=(0, 0))
        self.airline.set(self.flight_data["airline"])

        # Cities Frame
        cities_frame = ctk.CTkFrame(
            self.form_container, fg_color="transparent")
        cities_frame.pack(fill="x", pady=0)

        # From City (Start City)
        from_frame = ctk.CTkFrame(cities_frame, fg_color="transparent")
        from_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.from_city = self.form_components.create_form_row(
            from_frame,
            "From",
            required=True,
            field_type="text",
            placeholder="Departure"
        )
        self.from_city.pack(fill="x")
        self.from_city.insert(0, self.flight_data["departure"])

        # To City (End City)
        to_frame = ctk.CTkFrame(cities_frame, fg_color="transparent")
        to_frame.pack(side="left", fill="x", expand=True)
        self.to_city = self.form_components.create_form_row(
            to_frame,
            "To",
            required=True,
            field_type="text",
            placeholder="Destination"
        )
        self.to_city.pack(fill="x")
        self.to_city.insert(0, self.flight_data["destination"])

        # Dates Frame
        dates_frame = ctk.CTkFrame(self.form_container, fg_color="transparent")
        dates_frame.pack(fill="x", pady=(0, 15))

        # Depart Date
        depart_frame = ctk.CTkFrame(dates_frame, fg_color="transparent")
        depart_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.depart_date = self.form_components.create_form_row(
            depart_frame,
            "Depart Date",
            required=True,
            field_type="date"
        )
        self.setup_date_field(self.depart_date)
        self.depart_date.pack(fill="x")
        self.depart_date.insert(0, self.flight_data["depart_date"])

        # Return Date
        return_frame = ctk.CTkFrame(dates_frame, fg_color="transparent")
        return_frame.pack(side="left", fill="x", expand=True)
        self.return_date = self.form_components.create_form_row(
            return_frame,
            "Return Date",
            field_type="date"
        )
        self.setup_date_field(self.return_date)
        self.return_date.pack(fill="x")
        self.return_date.insert(0, self.flight_data["return_date"])

        # Action Buttons
        self.action_buttons = FormButtons(
            self.form_container,
            cancel_command=self.on_cancel,
            save_command=self.on_save,
        )
        self.action_buttons.pack(fill="x", pady=(20, 0))

    def get_clients(self) -> list[str]:
        """Get list of clients from the record manager"""
        clients = self.record_manager.records["client"]
        return [client["name"] for client in clients]

    def get_airlines(self) -> list[str]:
        """Get list of airlines from the record manager"""
        airlines = self.record_manager.records["airline"]
        return [airline["company_name"] for airline
                in airlines]

    def create_field(self, parent, label, required=False):
        """Create form field label"""
        label_text = f"{label} {'*' if required else ''}"
        ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Arial", 13)
        ).pack(anchor="w", pady=(0, 5))

    def setup_date_field(self, entry):
        """ Date Format """
        entry.bind('<KeyRelease>',
                   lambda event: DateFormatter.format_date_entry(entry))

    def validate_required_fields(self) -> tuple[bool, str]:
        """Validate all required fields are filled"""
        if self.client.get() == "Please select":
            return False, "Please select a client"

        if self.airline.get() == "Please select":
            return False, "Please select an airline"

        if not self.from_city.get():
            return False, "Please enter departure city"

        if not self.to_city.get():
            return False, "Please enter destination city"

        if not self.depart_date.get():
            return False, "Please enter departure date"

        return True, ""

    def validate_date_format(self, date_str):
        """Validate if date string matches DD/MM/YYYY format"""
        try:
            if date_str and date_str.count('/') == 2:
                day, month, year = map(int, date_str.split('/'))
                return (1 <= day <= 31 and
                        1 <= month <= 12 and
                        1000 <= year <= 9999)
        except ValueError:
            return False
        return False

    def on_cancel(self):
        """Handle cancel button click"""
        self.navigation_callback("flights")

    def on_save(self):
        """Handle save button click"""
        is_valid, error_message = self.validate_required_fields()
        if not is_valid:
            messagebox.showerror("Required Fields", error_message)
            return

        depart_date = self.depart_date.get()
        return_date = self.return_date.get()

        # Validate date formats
        if not self.validate_date_format(depart_date):
            messagebox.showerror(
                "Invalid Date Format",
                "Please enter departure date in DD/MM/YYYY format"
            )
            return

        if return_date and not self.validate_date_format(return_date):
            messagebox.showerror(
                "Invalid Date Format",
                "Please enter return date in DD/MM/YYYY format"
            )
            return

        new_flight = {
            "id": self.flight_data["id"],
            "type": "Flight",
            "client": self.client.get(),
            "airline": self.airline.get(),
            "departure": self.from_city.get(),
            "destination": self.to_city.get(),
            "depart_date": self.depart_date.get(),
            "return_date": self.return_date.get(),
            "created_at": self.flight_data["created_at"]
        }

        self.record_manager.update_record(
            "flight", new_flight["id"], new_flight)

        self.navigation_callback("flights")

    def on_delete(self):
        """Handle delete button click"""
        self.record_manager.delete_record("flight", self.flight_data["id"])
        self.navigation_callback("flights")
