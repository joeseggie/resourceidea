"""User account model.
"""
from sqlalchemy.dialects.postgresql import UUID

from app.common.models import BaseModel
from database import db


class UserAccount(BaseModel):
    """
    User account model.

    Args:
        db : Model
    """

    __tablename__ = 'user_account'

    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    email_confirmed = db.Column(db.Boolean, server_default='f')
    normalized_email = db.Column(db.String(128), unique=True)
    phone_number = db.Column(db.String(24), unique=True, nullable=True)
    phone_number_confirmed = db.Column(db.Boolean, nullable=True)
    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))

    def __repr__(self):
        return '<User %r>' % self.username
