"""Service plan model.
"""
from app import db


class ServicePlan(db.Model):
    """Service plan model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'service_plan'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Service plan %s(%f)' % self.name, self.price
