import hashlib
import os
from uuid import uuid4

import jwt
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID


def default_uuid_pk():
    return Column(UUID(as_uuid=True), primary_key=True, default=uuid4)


def generate_token(user_id: UUID, email: str) -> str:
    """
    Generate token

    Args:
        user_id: User ID.

        email: User email.

    Returns:
        Token
    """
    token_hash = generate_hash(user_id=user_id, email=email)
    key = os.environ.get('SECRET_KEY')
    token = jwt.encode({
            'user_id': user_id,
            'hash': token_hash
        },
        key)
    return token


def generate_hash(email: str, user_id: UUID) -> str:
    raw_input = f'{email}_{user_id}'
    sha256 = hashlib.sha256()
    sha256.update(raw_input.encode('utf-8'))
    return sha256.hexdigest()
