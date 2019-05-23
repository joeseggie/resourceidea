"""User account model.
"""
from app.common.models import BaseModel
from database import db


class UserAccount(BaseModel):
    """
    User account model.

    Args:
        db : Model
    """

    __tablename__ = 'user_account'

    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(128), unique=True)
    email_confirmed = db.Column(db.Boolean)
    normalized_email = db.Column(db.String(128), unique=True)
    phone_number = db.Column(db.String(24), unique=True)
    phone_number_confirmed = db.Column(db.Boolean)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))

    # employee = db.relationship(
    #     'Employee',
    #     uselist=False,
    #     backref='user_account')

    def __repr__(self):
        return '<User %r>' % self.normalized_email
