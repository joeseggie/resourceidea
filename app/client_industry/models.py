"""Client Industry model"""
from app.common.models import BaseModel
from database import db


class ClientIndustry(BaseModel):
    """Client Industry model"""

    __tablename__ = 'client_industry'

    name = db.Column(db.String(256), unique=True)
    name_slug = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return '<Client Industry %s>' % self.name
