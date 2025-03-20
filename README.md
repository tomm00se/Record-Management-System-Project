# Software Development In Practice - End of the Module - Group A - Travel Agent Portal

A desktop application for a specialist travel agent to manage client, flight, and airline records efficiently.

## 📌 Project Description

This project is a **Desktop Application** designed for a travel agent to manage various records. It supports three main types of records:

- **✈️ Client Records**: Personal details of clients.  
- **🛫 Flight Records**: Flight schedules, departure/arrival times, and airlines.  
- **🏢 Airline Company Records**: Information about airlines, including their contact and other relevant details.  

## 🚀 Features

- **🖥️ Graphical User Interface (GUI)**: An intuitive interface for easy interaction.  
- **💾 Persistent Storage**: Supports binary storage (using **Pickle**), **JSON**, or **JSON Lines (JSONL)** for data persistence.  
- **📂 Data Management**: Records are stored **in-memory** as a list of dictionaries.  
- **🔄 Automatic Save & Load**: Records are saved **automatically** upon application closure and loaded on startup.  
- **✅ Unit Testing**: Ensures the application functions as expected with **automatic tests**.  

## 📑 Record Format

- **🧑‍💼 Client Record**: Contains personal details such as name, contact info, etc.  
- **✈️ Flight Record**: Details of flight schedules, departure/arrival times, and associated airlines.  
- **🏢 Airline Record**: Information about airlines including name, contact, and other details.  

---

## 🔧 Installation & Setup  

### 📥 Clone the Repository  
```bash
git clone https://github.com/tomm00se/Record-Management-System-Project.git
# ⚙️ Install Dependencies
Install necessary Python libraries:

```bash
pip install -r requirements.txt
```

# ▶️ Run the Application
Start the application by running:

```bash
python app.py
```

# 📌 Usage

## 🚀 Start the Application
Launch the GUI.

## 📂 Perform Record Management Operations
Users can create, update, delete, search, and display records.

## 💾 Automatic Save
The application automatically saves records when closed and loads them on startup.

# 🧪 Unit Testing
Unit tests ensure that core functionalities are working as expected. To run the unit tests, follow these steps:

## 🏃‍♂️ Run the Tests
Make sure that you have the required testing libraries installed by checking the `requirements.txt`.

To run unit tests with unittest:

```bash
python -m unittest discover -s tests
```

Alternatively, if you prefer using pytest, you can run:

```bash
pytest
```

# ⚙️ Technical Details

## 🐍 Python Version
Python 3.8 or higher is recommended.

## 📚 Libraries Used:
- **Tkinter**: For GUI creation (pip install tk).
- **Pickle**: For binary storage (installed by default with Python).
- **JSON/JSONL**: For JSON file storage (pip install jsonlines for JSONL).
- **Unit Testing**: Uses built-in unittest or pytest for testing.

# ✨ Contributors
- 👨‍💻 Tommy Bowden
- 👩‍💻 Wing Lam Leona Wong
- 👩‍💻 Sude Şimşek

# 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

