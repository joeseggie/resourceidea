"""Employee model.
"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.common.models import BaseModel
from app.common.sqlalchemy_extensions import utcnow
from database import db


class Employee(BaseModel):
    """Employee model.

    Args:
        BaseModel: Base model.
    """
    __tablename__ = 'employee'

    file_number = db.Column(db.String(16), unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    other_names = db.Column(db.String(64), nullable=True)
    start_date = db.Column(db.DateTime, server_default=utcnow())
    termination_date = db.Column(db.DateTime, nullable=True)

    user_account_id = db.Column(UUID, db.ForeignKey('user_account.id'))
    user_account_account = relationship('UserAccount')

    organization_id = db.Column(UUID, db.ForeignKey('organization.id'))
    organization = relationship('Organization')

    def __repr__(self):
        return '<Employee %r %r>' % (self.first_name, self.last_name)
