# python-todo-app

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



