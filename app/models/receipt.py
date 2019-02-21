"""Receipt model.
"""
from database import db


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
    invoice = db.relationship('Invoice', backref='receipts')

    payment_method_id = db.Column(
        db.Integer, db.ForeignKey('payment_method.id')
    )
    payment_method = db.relationship('PaymentMethod', backref='receipts')
