"""
models.py

This module defines the database models for the application.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Represents a user in the database."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Returns the full name of the user."""
        return {"id": self.id, "name": self.name}

