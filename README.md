# Software Development In Practice

## End of Module - Travel Agent Portal

### Project Description
This project is a Desktop Application designed for a specialist travel agent to manage various records efficiently. The system supports three primary types of records:

Client Records
Flight Records
Airline Company Records
The application features a Graphical User Interface (GUI), allowing users to:

Create a Record
Delete a Record
Update a Record
Search and Display a Record

### Features
Graphical User Interface (GUI): An intuitive interface to interact with the application.
Persistent Storage: Supports binary storage (using pickle), JSON, or JSON Lines (JSONL) for data persistence.
Data Management: Records are stored in-memory as a list of dictionaries.
Automatic Save & Load: Records are saved automatically upon application closure and loaded upon startup.
Unit Testing: Unit tests ensure the reliability and correctness of the application.
Record Format
Client Record: Contains personal details such as name, contact, etc.
Flight Record: Details of flight schedules, departure/arrival times, and associated airlines.
Airline Record: Information about airlines including their name, contact, and other relevant details.

### Installation & Setup
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/your-repository-url.git
Install Dependencies:
Install necessary Python libraries:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application:
Start the application by running:

bash
Copy
Edit
python app.py
Usage
Start the application: Launch the GUI.
Perform Record Management Operations: Users can create, update, delete, search, and display records.
Automatic Save: The application will automatically save records when closed and load them on startup.
Unit Testing
Unit tests ensure that core functionalities are working as expected. To run the unit tests, follow these steps:

Ensure that you have the necessary testing libraries installed by checking requirements.txt.

### To run the unit tests

bash
Copy
Edit
python -m unittest discover -s tests
Or if using pytest:

bash
Copy
Edit
pytest


### Contributors
Contributor 1 Tommy Bowden 
Contributor 2 Wing Lam Leona Wong
Contributor 3 Sude Şimşek


### Technical Details
Python Version
Python 3.8 or higher is recommended for compatibility with libraries and features used in this project.

### Library Information
Here are the essential libraries for the project:

Tkinter: For creating the GUI.

Installation: pip install tk
Pickle: Used for serializing and deserializing objects for binary storage.

Installed by default with Python.
JSON / JSONL: For JSON file storage.

Installation: pip install jsonlines (if using JSONL format)
Unit Testing Framework:

unittest (built-in)
Or pytest (alternative): pip install pytest
