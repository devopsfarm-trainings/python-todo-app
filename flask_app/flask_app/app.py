from flask import Flask, jsonify, request
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


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"})

