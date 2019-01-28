"""Client industry model.
"""
from app import db


class ClientIndustry(db.Model):
    """Client industry model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'client_industry'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    company_id = db.Column(
        db.Integer,
        db.ForeignKey('company.id')
    )
    company = db.relationship(
        'Company',
        backref='client_industries'
    )
