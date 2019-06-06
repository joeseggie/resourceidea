from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class UserRole(BaseModel):
    """
    UserRole model.

    Args:
        BaseModel: Base model.
    """

    __tablename__ = 'user_role'

    user_account_id = db.Column(UUID, db.ForeignKey('user_account.id'))
    role_id = db.Column(UUID, db.ForeignKey('role.id'))

    user = relationship('UserAccount')
    role = relationship('Role')

    __table_args__ = (UniqueConstraint('user_account_id', 'role_id', name='ux_useraccountid_roleid'),)
