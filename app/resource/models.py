"""app.resource.models module"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class Resource(BaseModel):
    """
    Resource model.
    """

    __tablename__ = 'resource'

    color = db.Column(db.String(7), nullable=True)
    is_active = db.Column(db.Boolean, server_default='t')

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    employee_id = db.Column(UUID, db.ForeignKey('employee.id'))
    employee = relationship('Employee', backref=backref('resource', uselist=False))
