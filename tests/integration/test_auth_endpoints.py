from uuid import UUID

from flask import json


def test_signup(app, session, fake_person, fake_profile):
    # Arrange
    client = app.test_client()
    request_body = {
        "organization": fake_profile.profile()['company'],
        "username": fake_profile.profile()['username'],
        "password": "strong_password",
        "confirm_password": "strong_password",
        "email": "joeseggie@gmail.com",
        "first_name": fake_person.first_name(),
        "last_name": fake_person.last_name()
    }

    # Act
    client_response = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert client_response.status_code == 201
    assert 'status' in output
    assert output['status'] == 'OK'
    assert 'data' in output
    assert isinstance(output['data'], dict)
    assert isinstance(UUID(output['data']['user_id']), UUID)
    assert isinstance(UUID(output['data']['organization_id']), UUID)


def test_signup_organization_exists(app, session, fake_person, fake_profile):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Organization 1',
        'username': 'test123',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'email': 'joeseggie@gmail.com',
        'first_name': fake_person.first_name(),
        'last_name': fake_person.last_name()
    }

    # Act
    client_response = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert client_response.status_code == 400
    assert 'status' in output
    assert output['status'] == 'Organization name already exists'


def test_user_signup_email_exists(app, session, fake_person):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Organization 12',
        'username': 'test123',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'email': 'mail@example.com',
        'first_name': fake_person.first_name(),
        'last_name': fake_person.last_name()
    }

    # Act
    result = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(result.get_data(as_text=True))

    # Assert
    assert result.status_code == 400
    assert 'status' in output
    assert output['status'] == 'Email already exists'


def test_user_signup_phone_number_exists(
        app,  session, fake_person):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Organization 12',
        'username': 'test_user',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'phone_number': '000-0000-111',
        'email': 'e1.mail@example.com',
        'first_name': fake_person.first_name(),
        'last_name': fake_person.last_name()
    }

    # Act
    result = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(result.get_data(as_text=True))

    # Assert
    assert result.status_code == 400
    assert 'status' in output
    assert output['status'] == 'Phone number already exists'


def test_user_signup_username_exists(app, session, fake_person):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Organization 12',
        'username': 'test_user',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'phone_number': '000-0010-111',
        'email': 'e1.mail@example.com',
        'first_name': fake_person.first_name(),
        'last_name': fake_person.last_name()
    }

    # Act
    result = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(result.get_data(as_text=True))

    # Assert
    assert result.status_code == 400
    assert 'status' in output
    assert output['status'] == 'Username is already taken'
