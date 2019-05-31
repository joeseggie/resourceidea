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


def create_user(
                organization_id: UUID,
                username: str,
                password: str,
                email: str,
                **kwargs) -> UserAccount:
    """
    Create a new user.

    Args:
        organization_id {UUID}: Id for the user's organization.
        username {str}: User's username.
        password {str}: User's password.
        email {str}: User's email.

    Returns:
        UserAccount: New user account.
    """
    new_user_account = UserAccount()
    new_user_account.username = username
    new_user_account.password = password
    new_user_account.email = email
    new_user_account.organization_id = organization_id
    new_user_account.phone_number = kwargs.get('phone_number', None)

    return UserRepository.create(new_user_account)


def get_user(user_id: UUID) -> UserAccount:
    """
    Get a user by Id.

    Args:
        user_id {UUID}: Id of the user to be returned.

    Returns:
        UserAccount: User account whose Id was supplied.
    """
    return UserRepository.get_one_by_id(model_id=user_id)


def get_user_by_username(username: str, **kwargs) -> UserAccount:
    """
    Get a user by username

    Args:
        username {str}: User's username.

    Returns:
        UserAccount: User account whose username is supplied.
    """
    filter_field = {'username': username}
    return UserRepository.get_one_by_field(**filter_field)


def get_user_by_email(email: str, **kwargs) -> UserAccount:
    """
    Get a user by email

    Args:
        email {str}: User's email.

    Returns:
        UserAccount: User account whose email is supplied.
    """
    filter_field = {'email': email}
    return UserRepository.get_one_by_field(**filter_field)


def get_user_by_phone_number(**kwargs) -> UserAccount:
    """
    Get a user by phone_number

    Args:
        phone_number {str}: User's phone number

    Returns:
        UserAccount: User account whose email is supplied.
    """
    if 'phone_number' in kwargs:
        phone_number = kwargs.get('phone_number', None)
        if phone_number:
            filter_field = {'phone_number': phone_number}
            return UserRepository.get_one_by_field(**filter_field)
    return


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
