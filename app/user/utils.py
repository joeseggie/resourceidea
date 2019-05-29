from flask import abort
from typing import List
from uuid import UUID

from .models import UserAccount
from .repositories import UserRepository


def get_all_users(**kwargs) -> List[UserAccount]:
    """
    Get a list of user accounts.

    Returns:
        List[UserAccount]: List of user accounts.
    """
    return UserRepository.get_all(**kwargs)


def create_user(**kwargs) -> UserAccount:
    """
    Create a new user account.

    Returns:
        UserAccount: User account created.
    """
    return UserRepository.create(**kwargs)


def get_user(user_id: UUID) -> UserAccount:
    """
    Get a user by Id.

    Args:
        user_id {UUID}: Id of the user to be returned.

    Returns:
        UserAccount: User account whose Id was supplied.
    """
    return UserRepository.get_one_by_id(model_id=user_id)


def update_user(user_id: UUID, **kwargs) -> UserAccount:
    """
    Updates a user account's details.

    Args:
        user_id {UUID}: Id of the user to be updated.

    Returns:
        UserAccount: User account whose details were updated.
    """
    return UserRepository.update(user_id, **kwargs)


def delete_user(user_id: UUID):
    """
    Deletes a user account whose Id has bee provided.

    Args:
        user_id {UUID}: Id of the user account to be deleted.
    """
    return UserRepository.delete_by_id(model_id=user_id)


def confirm_email(user_id: UUID, email: str):
    """
    Confirm user account email.

    Args:
        user_id {UUID}: User account Id.
        email {str}: Email to be confirmed.
    """
    user_account = UserRepository.get_one_by_id(model_id=user_id)
    if not user_account:
        abort(404, 'User account does not exist')
    if email.lower() != user_account.email.lower():
        abort(400, 'Email confirmation failed')
    UserRepository


def confirm_phone_number(user_id: UUID, phone_number: str):
    """
    Confirm user account phone number.

    Args:
        user_id {UUID}: User account Id.
        phone_number {str}: Phone number to be confirmed.
    """
    pass
