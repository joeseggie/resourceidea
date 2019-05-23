from app.common.utils import default_uuid_pk
from app.common.sqlalchemy_extensions import utcnow
from database import db


class BaseModel(db.Model):
    __abstract__ = True

    id = default_uuid_pk()
    created = db.Column(db.DateTime, server_default=utcnow())
    last_update = db.Column(db.DateTime, onupdate=utcnow())
