# Software Development In Practice End of the Module Group A Travel Agent Portal

A desktop application for a specialist travel agent to manage client, flight, and airline records for operation purpose.

## 📌 Project Description

### System Structure
```bash
src/
  ├── assets/         # Assets management
  ├── data/           # Backend Operations (Data Processing)
  ├── gui/            # Frontend Operations (GUI)
  │   ├── pages/      # Pages
  │   └── components/ # UI components
  ├── record/         # Records Management (Data Storage)
  └── tests/          # Test files
```
### Repository
The repository supports the following:

**🖥️ Graphical User Interface (GUI)** <br/>
- An intuitive interface for easy interaction

**💾 Persistent Storage** <br/>
- Supports binary storage (using **Pickle**), **JSON**, or **JSON Lines (JSONL)** for data persistence

**📂 Data Management** <br/>
- Supports **CRUD operations** (Create, Read, Update, Delete) <br/>
- **In-memory** data storage <br/>
- **RecordManager:** Custom record management system

**🔄 Automatic Save & Load** <br/>
- Records are saved **automatically** upon application closure and loaded on startup

**✅ Unit Tests** <br/>
- Ensures the application functions as expected with **automatic tests**

**✅ Performance Test** <br/>
- Ensures the application loaded, updated and deleted records in a reasonable time

## 🚀 Application Features

**🛫 Flight Records** <br/>
- Able to add, update, and delete flight records with details, such as client name, flight schedule, departure, destination and associated airline

**✈️ Client Records** <br/>
- Able to add, update, and delete client records with details, such as name and associated information

**🏢 Airline Records** <br/>
- Able to add, update, and delete airline records with their company names and location base

## 🔧 Installation & Setup  

### 📥 Clone the Repository
```bash
git clone https://github.com/tomm00se/Record-Management-System-Project.git
```
### ⚙️ Install Dependencies
Install necessary Python libraries:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Application
Start the application by running:

```bash
python src/main.py
```

## 📌 Usage

### 🚀 Start the Application
- Launch the GUI.

### 📂 Perform Record Management Operations
- Users can create, update, delete, search, and display records.

### 💾 Automatic Save
- The application automatically saves records when closed and loads them on startup.

## 🧪 Testing

### 🏃‍♂️ Run the Unit Tests

**Backend Operation Test**
```bash
python -m unittest src/test/data_test.py -v
```
**GUI Test**
```bash
python -m unittest src/test/record_gui3_unit_test.py -v
```

### 🏃‍♂️ Run the Performance Test

```bash
python src/test/performance_test.py
```

## ⚙️ Technical Details

### 🐍 Python Version
Python 3.8 or higher is recommended.

#### Frontend
`customTkinter` Modern GUI framework, an enhanced version of tkinter

`tkinter` Python's standard GUI library

`CTk` CustomTkinter's main window class

#### Backend
`json` JSON format storage

`jsonlines` JSONL format storage

`pickle` Binary format storage

#### Unit Testing
`unittest` Built-in testing library

## ✨ Contributors
👨‍💻 Tommy Bowden <br/>
👩‍💻 Wing Lam Leona Wong <br/>
👩‍💻 Sude Şimşek

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.