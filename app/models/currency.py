"""Currency model.
"""
from app import db


class Currency(db.Model):
    """Currency model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'currency'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(3))
    description = db.Column(db.String(64))

    company_id = db.Column(
        db.Integer,
        db.ForeignKye('company.id')
    )
    company = db.relationship(
        'Company',
        backref=db.backref(
            'currencies',
            lazy=True
        )
    )
