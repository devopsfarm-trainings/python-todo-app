# Steps for Running Frontend Code 

# Flask Frontend Project

This is a simple Flask web application with a frontend setup using HTML, CSS, and JavaScript.

## Project Structure

```
/flask_frontend
│── /static
│   ├── styles.css      # Stylesheet for the frontend
│   ├── script.js       # JavaScript file for frontend interactions
│── /templates
│   ├── index.html      # Main HTML file
│── app.py              # Main Flask application file
│── requirements.txt    # List of required Python packages
```

## Installation and Setup

### Prerequisites
Ensure you have Python 3 installed on your system. You also need `pip` and `virtualenv`.

### Steps to Set Up the Project

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd flask_frontend
   ```

2. **Install dependencies**
   ```bash
   apt install python3-dev python3-pip
   ```

3. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Modify `index.html` in the `templates/` folder for UI changes.
- Update `styles.css` and `script.js` in `static/` for frontend modifications.
- Edit `app.py` to change Flask routes and backend logic.


# Flask App with SQLite Database

This project is a simple **Flask Web Application** with an **SQLite database**. It includes a frontend (HTML, CSS, JavaScript) and a backend (Flask, SQLAlchemy). The application allows users to interact with a database via a REST API.

---




## **Project Structure**

```
/flask_app
│── /static
│   ├── styles.css        # Frontend CSS styles
│   ├── script.js         # Frontend JavaScript logic
│── /templates
│   ├── index.html        # Main HTML template
│── models.py             # SQLAlchemy models
│── app.py                # Main Flask application
│── requirements.txt      # Python dependencies
│── config.py             # Configuration settings
```

---

## **1. Installation**

### **Clone the Repository**

```bash
git clone <your-repo-url>
cd flask_app
```

### **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## **2. Database Setup**

The database is automatically created when running the app.

However, to manually initialize it:

```bash
python
```

Then run:

```python
from app import db
db.create_all()
exit()
```

This will create **database.db** in the project directory.

---

## **3. Running the Flask App**

Start the Flask server:

```bash
python app.py
```

The app will be available at:\
📌 [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

---

## **4. API Endpoints**

### **Fetch All Users**

**Request:**

```bash
curl -X GET http://127.0.0.1:5000/api/users
```

**Response:**

```json
[
    {
        "id": 1,
        "name": "John Doe"
    }
]
```

---

### **Add a New User**

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe"}'
```

**Response:**

```json
{
    "message": "User added successfully!",
    "user": {
        "id": 1,
        "name": "John Doe"
    }
}
```

---

## **5. Frontend Usage**

- Open [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/) in a browser.
- Click the **button** to fetch users from the API.
- Enter a **name** in the input field and click "Add User" to send data to the database.

---

## **6. Database File**

- The SQLite database file is named **database.db**.
- To view the contents, use **SQLite CLI**:
  ```bash
  sqlite3 database.db
  ```
  Then run:
  ```sql
  SELECT * FROM user;
  ```
- To reset the database, delete the file:
  ```bash
  rm database.db
  ```

---

## **7. Configuration**

Modify **config.py** for different settings, including database connections.

---

## **8. Notes**

- This app uses **Flask + SQLite**, making it lightweight and easy to deploy.
- To switch databases (e.g., PostgreSQL), update `config.py` and `SQLALCHEMY_DATABASE_URI`.

---



