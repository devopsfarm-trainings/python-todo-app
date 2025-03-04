Project Structure

/flask_app
│── /static
│   ├── styles.css
│   ├── script.js
│── /templates
│   ├── index.html
│── /models.py
│── app.py
│── requirements.txt
│── config.py


1. Install Dependencies
Before running the project, install the required packages:

<pip install flask flask-sqlalchemy psycopg2>


2. Configuration File (config.py)
This file stores the database connection settings.

##import os

##BASE_DIR = os.path.abspath(os.path.dirname(__file__))
##DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"


3. Database Models (models.py)
Defines a User model with an id and name.

(from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}
)


4. Flask API (app.py)
This Flask API fetches data from SQLite and returns JSON.

(from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, User
from config import DATABASE_URL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Fetch all users
@app.route("/api/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Add a new user
@app.route("/api/users", methods=["POST"])
def add_user():
    data = request.json
    new_user = User(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!", "user": new_user.to_dict()}), 201

if __name__ == "__main__":
    app.run(debug=True)

)


5. Frontend - HTML (templates/index.html)
A simple UI to display and add users.

(<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Database Integration</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Flask Database Integration</h1>

    <input type="text" id="username" placeholder="Enter name">
    <button onclick="addUser()">Add User</button>

    <h2>Users List</h2>
    <ul id="userList"></ul>

    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
)



6. JavaScript (static/script.js)
Fetches and adds users via API.

(document.addEventListener("DOMContentLoaded", fetchUsers);

function fetchUsers() {
    fetch("/api/users")
        .then(response => response.json())
        .then(users => {
            let userList = document.getElementById("userList");
            userList.innerHTML = "";
            users.forEach(user => {
                let li = document.createElement("li");
                li.textContent = user.name;
                userList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching users:", error));
}

function addUser() {
    let name = document.getElementById("username").value;
    fetch("/api/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
    })
    .then(response => response.json())
    .then(() => {
        fetchUsers();
        document.getElementById("username").value = "";
    })
    .catch(error => console.error("Error adding user:", error));
}
)


7. CSS (static/styles.css)
Basic styling.

(body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 50px;
}

input {
    padding: 8px;
    margin: 10px;
}

button {
    padding: 10px 20px;
    cursor: pointer;
}

ul {
    list-style-type: none;
}
)



8. Running the Project
Run the app

1.Run the app
< python app.py>

2.Test API
.fetch all the users:
<curl http://127.0.0.1:5000/api/users>

.Add a user:
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe"}'












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



