"""Payment method model.
"""
from database import db


class PaymentMethod(db.Model):
    """Payment method model.

    Parameters
    ----------
        db : Model
    """
    __tablename__ = 'payment_method'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64))

    def __repr__(self):
        return '<Payment method %s>' % self.description
