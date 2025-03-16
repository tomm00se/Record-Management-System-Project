""" Edit Flight Page Module """

import customtkinter as ctk
from src.gui.pages.base import BasePage
from src.data.record_manager import RecordManager

class EditFlightPage(BasePage):
    """ Edit Flight Page Class """

    def __init__(self, parent, navigation_callback, record_manager: RecordManager, flight_data=None):
        self.record_manager = record_manager

        # Initialize the base page first
        super().__init__(parent, navigation_callback)

        # Store flight data
        self.flight_data = flight_data

        # Create page header only
        self.create_header(
            title="Edit Flight",
            description="Edit the travel details to update the flight record"
        )

        self.create_form()

    def create_form(self):
        """Create the form for adding a new flight"""
        # Form container
        form_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=15, pady=15)

        # Client Selection
        self.create_field(form_frame, "Client", True)
        self.client = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter client name"  # This shows helper text when empty
        )
        self.client.pack(fill="x", pady=(0, 15))
        self.client.insert(0, self.flight_data["client"])

        # Airline Selection
        self.create_field(form_frame, "Airline", True)
        self.airline = ctk.CTkOptionMenu(
            form_frame,
            values=self.get_airlines()
        )
        self.airline.pack(fill="x", pady=(0, 15))
        self.airline.set(self.flight_data["airline"])

        # Cities Frame
        cities_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        cities_frame.pack(fill="x", pady=(0, 15))

        # From City (Start City)
        from_frame = ctk.CTkFrame(cities_frame, fg_color="transparent")
        from_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.create_field(from_frame, "From", True)
        self.from_city = ctk.CTkEntry(
            from_frame,
            placeholder_text="Enter departure city"
        )
        self.from_city.pack(fill="x")
        self.from_city.insert(0, self.flight_data["departure"])

        # To City (End City)
        to_frame = ctk.CTkFrame(cities_frame, fg_color="transparent")
        to_frame.pack(side="left", fill="x", expand=True)
        self.create_field(to_frame, "To", True)
        self.to_city = ctk.CTkEntry(
            to_frame,
            placeholder_text="Enter destination city"
        )
        self.to_city.pack(fill="x")
        self.to_city.insert(0, self.flight_data["destination"])

        # Dates Frame
        dates_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        dates_frame.pack(fill="x", pady=(0, 15))

        # Depart Date
        depart_frame = ctk.CTkFrame(dates_frame, fg_color="transparent")
        depart_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.create_field(depart_frame, "Depart Date", True)
        self.depart_date = ctk.CTkEntry(
            depart_frame,
            placeholder_text="DD/MM/YYYY"
        )
        self.depart_date.pack(fill="x")
        self.depart_date.insert(0, self.flight_data["depart_date"])

        # Return Date
        return_frame = ctk.CTkFrame(dates_frame, fg_color="transparent")
        return_frame.pack(side="left", fill="x", expand=True)
        self.create_field(return_frame, "Return Date")
        self.return_date = ctk.CTkEntry(
            return_frame,
            placeholder_text="DD/MM/YYYY"
        )
        self.return_date.pack(fill="x")
        self.return_date.insert(0, self.flight_data["return_date"])

        # Buttons
        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(20, 0))

        # Cancel Button
        ctk.CTkButton(
            button_frame,
            text="Cancel",
            command=self.on_cancel,
            fg_color="#E5E5EA",
            text_color="#000000"
        ).pack(side="left", padx=(0, 10))


        # Save Button
        ctk.CTkButton(
            button_frame,
            text="Save",
            command=self.on_save
        ).pack(side="left")
        
        button_frame_delete = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame_delete.pack(fill="x", pady=(20, 0))

        # Delete Button
        ctk.CTkButton(
            button_frame_delete,
            text="Delete",
            command=self.on_delete,
            fg_color="#FF3B30",
            text_color="#FFFFFF"
        ).pack(side="left", padx=(0, 10))
        
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

    def on_cancel(self):
        """Handle cancel button click"""
        self.navigation_callback("flights")

    def on_save(self):
        """Handle save button click"""
        
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
        
        self.record_manager.update_record("flight", new_flight["id"], new_flight)
        
        self.navigation_callback("flights")

    def on_delete(self):
        """Handle delete button click"""
        self.record_manager.delete_record("flight", self.flight_data["id"])
        self.navigation_callback("flights")