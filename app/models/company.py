"""Company model
"""
from database import db


class Company(db.Model):
    """Company model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    name_stub = db.Column(db.String(256))
    address = db.Column(db.String(256))

    def __repr__(self):
        return '<Company %s>' % self.name
