"""Invoice model.
"""
from app import db


class Invoice(db.Model):
    """Invoice model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'invoice'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    invoice_date = db.Column(db.DateTime)
    invoice_period_start = db.Column(db.DateTime)
    invoice_period_end = db.Column(db.DateTime)

    subscription_id = db.Column(
        db.Integer,
        db.ForeignKey('subscription.id')
    )
    subscription = db.relationship(
        'Subscription',
        backref='invoices'
    )
