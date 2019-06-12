"""
Test UserRepository
"""
from app.user.models import UserAccount
from app.user.repositories import UserRepository


def test_confirm_email(session, fake_profile):
    # Arrange
    fake_email = fake_profile.profile()['mail']
    fake_user = UserAccount(
        username=fake_profile.profile()['username'],
        password='strong_password',
        email=fake_email,
        normalized_email=fake_email.upper())
    test_user = UserRepository.create(fake_user)
    confirmation_test = {'email_confirmed': True}
    before_confirmation = test_user.email_confirmed

    # Act
    result = UserRepository.confirm_email(test_user.id, **confirmation_test)

    # Assert
    assert before_confirmation is False
    assert result.email_confirmed is True
