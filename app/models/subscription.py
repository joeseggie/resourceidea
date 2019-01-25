"""Subscription model.
"""
from app import db


class Subscription(db.Model):
    """Subscription model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'subscription'

    id = db.Column(db.Integer, primary_key=True)
    started = db.Column(db.DateTime)
    ended = db.Column(db.DateTime)

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('company.id')
    )
    company = db.relationship(
        'Company',
        backref=db.backref(
            'posts',
            lazy=True
        )
    )
