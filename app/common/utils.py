from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID


def default_uuid_pk():
    return Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
