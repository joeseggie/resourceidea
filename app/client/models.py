"""Client model.
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class Client(BaseModel):
    """
    Client model.

    Args:
        db.Model: Base model.
    """

    __tablename__ = 'client'

    name = db.Column(db.String(256))
    name_slug = db.Column(db.String(256))
    address = db.Column(db.String(256), nullable=True)

    client_industry_id = db.Column(
        UUID,
        db.ForeignKey('client_industry.id'),
        nullable=True)
    client_industry = relationship('ClientIndustry')

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    def __repr__(self):
        return '<Client %s>' % self.name
