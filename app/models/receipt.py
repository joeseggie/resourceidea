"""Receipt model.
"""
from app import db


class Receipt(db.Model):
    """Receipt model.

    Parameters
    ----------
        db : Model
    """
    __tablename__ = 'receipt'

    id = db.Column(db.Integer, primary_key=True)
    amount_paid = db.Column(db.Float)
    payment_date = db.Column(db.DateTime)

    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    invoice = db.relationship('Invoice', backref=db.backref(
        'receipts',
        lazy=True
    ))
