"""User account model.
"""
from app import db


class UserAccount(db.Model):
    """User account model.

    Parameters
    ----------
    db : Model
    """
    __tablename__ = 'user_account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    email_confirmed = db.Column(db.Boolean)
    normalized_email = db.Column(db.String(128))
    phone_number = db.Column(db.String(24))
    phone_number_confirmed = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.normalized_email
