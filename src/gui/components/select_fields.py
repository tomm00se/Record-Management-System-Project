"""
Reusable components for selecting data in the application.
"""
class SelectCountry:
    """Country selection component with predefined country list"""

    # Class-level constant for countries
    COUNTRIES = [
        "Argentina", "Australia", "Austria", "Belgium", "Brazil",
        "Croatia", "Denmark", "Fiji", "Finland", "France", "Germany",
        "Greece", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
        "Israel", "Italy", "Jamaica", "Japan","Korea", "Singapore",
        "South Africa", "South Sudan", "Spain",  "Sweden", "Switzerland",
        "Taiwan", "Ukraine", "United Arab Emirates", "United Kingdom", "United States"
    ]

    @classmethod
    def create_field(cls, parent):
        """Create a country selection combobox"""
        import customtkinter as ctk

        return ctk.CTkComboBox(
            parent,
            values=cls.COUNTRIES,
            fg_color="white",
            bg_color="transparent",
            border_color="#565B5E",
            text_color="black",
            dropdown_fg_color="white",
            dropdown_text_color="black",
            dropdown_hover_color="#E6E6E6",
            button_color="#565B5E",
            button_hover_color="#666666",
            height=35,
            corner_radius=5,
            placeholder_text="Select Country"
        )
