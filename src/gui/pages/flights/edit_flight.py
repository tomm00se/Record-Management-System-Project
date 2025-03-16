""" Edit Flight Page Module """

import customtkinter as ctk
from ..base import BasePage

class EditFlightPage(BasePage):
    """ Edit Flight Page Class """

    def __init__(self, parent, navigation_callback, flight_data=None):
        print("EditFlightPage - Initializing")  # Debug print

        # Initialize the base page first
        super().__init__(parent, navigation_callback)

        # Store flight data
        self.flight_data = flight_data

        # Create page header only
        self.create_header(
            title="Edit Flight",
            description="Edit the travel details to update the flight record"
        )

        print("EditFlightPage - Header created")  # Debug print
