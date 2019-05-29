from sqlalchemy.dialects.postgresql import UUID

from app.common.sqlalchemy_extensions import utcnow
from database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        UUID,
        primary_key=True,
        server_default=db.func.uuid_generate_v4())
    created = db.Column(db.DateTime, server_default=utcnow())
    last_update = db.Column(
        db.DateTime,
        server_default=utcnow(),
        onupdate=utcnow())
