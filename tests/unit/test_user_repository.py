"""
Test UserRepository
"""
from app.user.models import UserAccount
from app.user.repositories import UserRepository


def test_confirm_email(session, fake_profile, fake_misc):
    # Arrange
    fake_email = fake_profile.profile()['mail']
    fake_user = UserAccount(
        username=fake_profile.profile()['username'],
        password=fake_misc.password(length=10),
        email=fake_email,
        normalized_email=fake_email.upper())
    test_user = UserRepository.create(fake_user)
    confirmation_test = {'email_confirmed': True}
    not_confirmed = test_user.email_confirmed

    # Act
    result = UserRepository.confirm_email(test_user.id, **confirmation_test)

    # Assert
    if not_confirmed is True:
        raise AssertionError()

    if result.email_confirmed is False:
        raise AssertionError()
