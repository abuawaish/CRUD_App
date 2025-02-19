# CRUD_App

## Overview
CRUD_App is a simple web application that demonstrates basic CRUD (Create, Read, Update, Delete) operations. It is built using Python for the backend and HTML for the frontend. This project is ideal for understanding the fundamental operations used in web applications.

## Features
- Create new records
- Read existing records
- Update records
- Delete records

## Technologies Used
- **Python**: Backend development
- **HTML**: Frontend templates

## Directory Structure
The directory structure of the project is as follows:

```bash
  CRUD_App/
        ├── app.py                 # Main application file
        ├── requirements.txt       # Dependencies required to run the app
        ├── static/                # For holding static images
        │   ├── config.png         # Header logo for config_mysql page
        │   └── mysql.png          # Header logo for home page
        ├── templates/             # HTML templates for the frontend
        │   ├── config_mysql.html  # For self configuration mysql database
        │   └── home.html          # User Interface for executing sql query
        ├── .gitignore             # Git ignore file
        ├── LICENSE                # Project license
        └── README.md              # Project documentation
```


## Installation

### Prerequisites
- Python 3.8 or later installed on your system
- Pip package manager installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/abuawaish/CRUD_App.git
   cd CRUD_App
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
   ```bash
   python app.py
   ```

### Usage
- Access the application in your web browser.
- Use the interface to create, view, update, and delete records.

### License
- This project is licensed under the MIT License. See the LICENSE file for details.
