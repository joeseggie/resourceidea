"""Subscription model.
"""
from database import db


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
        db.ForeignKey('organization.id')
    )
    company = db.relationship(
        'Company',
        backref='subscriptions')
