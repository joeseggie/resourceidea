"""Employee model.
"""
from app import db


class Employee(db.Model):
    """Employee model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    file_number = db.Column(db.String(16))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    join_date = db.Column(db.DateTime)
    termination_date = db.Column(db.DateTime)
