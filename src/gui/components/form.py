"""Form Components Module"""
import customtkinter as ctk

class FormComponents:
    """Reusable Form Components"""
    def __init__(self):
        # Common Input Fields Style
        self.input_style = {
            "font": ("Arial", 16),
            "fg_color": "white",
            "border_color": "#dfe4ea",
            "border_width": 1,
            "text_color": "#000000",
            "corner_radius": 3,
            "height": 38,
        }

        # Common Option Menu Style
        self.option_style = {
            "font": ("Arial", 16),
            "fg_color": "white",
            "text_color": "black",
            "button_color": "white",
            "button_hover_color": "white",
            "dropdown_fg_color": "white",
            "dropdown_text_color": "#007aff",
            "dropdown_hover_color": "white",
            "corner_radius": 3,
            "height": 38,
        }

    def create_field_label(self, parent, label, required=False):
        """Create form field label"""
        label_text = f"{label} {'*' if required else ''}"
        return ctk.CTkLabel(
            parent,
            text=label_text,
            font=("Arial", 13)
        )

    def create_text_input(self, parent, placeholder="", **kwargs):
        """Create a text input field"""
        return ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            **{**self.input_style, **kwargs}
        )

    def create_option_menu(self, parent, values, **kwargs):
        """Create an option menu"""
        return ctk.CTkOptionMenu(
            parent,
            values=values,
            **{**self.option_style, **kwargs}
        )

    def create_date_input(self, parent, placeholder="DD/MM/YYYY", **kwargs):
        """Create a date input field"""
        date_input = self.create_text_input(parent, placeholder, **kwargs)
        date_input.bind('<KeyRelease>', lambda e: self.format_date(date_input))
        return date_input

    def create_form_row(self, parent, label, required=False, field_type="text", **kwargs):
        """Create a complete form row with label and field"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 15))

        # Create label
        label = self.create_field_label(frame, label, required)
        label.pack(anchor="w", pady=(0, 5))

        # Create field based on type
        field = None
        if field_type == "text":
            field = self.create_text_input(frame, **kwargs)
        elif field_type == "option":
            field = self.create_option_menu(frame, **kwargs)
        elif field_type == "date":
            field = self.create_date_input(frame, **kwargs)
        
        # Pack the field if it was created
        if field:
            field.pack(fill="x")
        return field

    def format_date(self, entry):
        """Format date as DD/MM/YYYY while typing"""
        text = entry.get()

        # Remove any non-digit characters
        cleaned_text = ''.join(filter(str.isdigit, text))

        # Limit to 8 digits (DDMMYYYY)
        cleaned_text = cleaned_text[:8]

        formatted_date = ""

        # Format the date with slashes
        if len(cleaned_text) > 0:
            # Add day
            day = cleaned_text[:2] if len(cleaned_text) >= 2 else cleaned_text
            # Ensure day is not > 31
            if len(day) == 2 and int(day) > 31:
                day = "31"
            formatted_date += day

            # Add month
            if len(cleaned_text) > 2:
                month = cleaned_text[2:4]
                # Ensure month is not > 12
                if len(month) == 2 and int(month) > 12:
                    month = "12"
                formatted_date += "/" + month

            # Add year
            if len(cleaned_text) > 4:
                formatted_date += "/" + cleaned_text[4:]

        # Update entry content
        entry.delete(0, 'end')
        entry.insert(0, formatted_date)
