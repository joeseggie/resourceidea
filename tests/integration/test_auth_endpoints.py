from uuid import UUID

from flask import json


def test_signup(app, session):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Test xx organization',
        'username': 'test123',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'email': 'joeseggie@gmail.com'
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
    assert output['data']['organization'] == 'Test xx organization'
    assert output['data']['username'] == 'test123'
    assert output['data']['organization_slug'] == 'test-xx-organization'
    assert isinstance(UUID(output['data']['user_id']), UUID)
    assert isinstance(UUID(output['data']['organization_id']), UUID)


def test_signup_organization_exists(app, session):
    # Arrange
    client = app.test_client()
    request_body = {
        'organization': 'Organization 1',
        'username': 'test123',
        'password': 'strong_password',
        'confirm_password': 'strong_password',
        'email': 'joeseggie@gmail.com'
    }

    # Act
    client_response = client.post('/api/v0.1/signup', json=request_body)
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert client_response.status_code == 400
    assert 'status' in output
    assert output['status'] == 'Organization name already exists'
