from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.common.models import BaseModel
from database import db


class Role(BaseModel):
    """
    Role model.

    Args:
        BaseModel: Base model.
    """

    __tablename__ = 'role'

    name = db.Column(db.String(256), unique=True)
    normalized_name = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return '<Role %s>' % self.name
