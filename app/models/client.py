"""Client model.
"""
from app import db


class Client(db.Model):
    """Client model.

    Paramaters
    ---------
    db : Model
    """
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    name_stub = db.Column(db.String(256))
    address = db.Column(db.String(256))

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('company.id')
    )
    company = db.relationship(
        'Company',
        backref=db.backref(
            'clients',
            lazy=True
        )
    )