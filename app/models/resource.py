"""Resource model.
"""
from app import db


class Resource(db.Model):
    """Resource model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'resource'

    id = db.Column(db.Integer, primary_key=True)
    charge_rate = db.Column(db.Float)
    color = db.Column(db.String(7))
    is_active = db.Column(db.Boolean)
