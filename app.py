"""Flask application for user management.

This app provides APIs for:
- Fetching users
- Adding a user
- Deleting a user
- Rendering a template
"""

from flask import Flask, jsonify, request, render_template
from models import db, User
from config import DATABASE_URL

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    """Return a JSON response with a sample message."""
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/users", methods=["GET"])
def get_users():
    """Retrieve all users from the database."""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route("/api/users", methods=["POST"])
def add_user():
    """Add a new user to the database."""
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_user = User(name=data["name"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added successfully!", "user": new_user.to_dict()}), 201

@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user by their ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
