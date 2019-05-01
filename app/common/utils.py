from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy_utils import UUIDType


def default_uuid_pk():
    return Column(UUIDType(binary=False), primary_key=True, default=uuid4)
