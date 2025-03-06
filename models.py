"""
models.py

This module defines the database models for the application.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user in the database.

    Attributes:
        id (int): The primary key identifier for the user.
        name (str): The name of the user.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """
        Converts the user object into a dictionary.

        Returns:
            dict: A dictionary representation of the user.
        """
        return {"id": self.id, "name": self.name}

