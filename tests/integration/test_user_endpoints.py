from flask import json


def test_create_user(app, session):
    # Arrange
    client = app.test_client()

    # Act
    client_response = client.post('/api/v0.1/users',
                                  json=dict(
                                      username='test1',
                                      password='password'))
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert 'code' in output
    assert isinstance(output['code'], int)
    assert output['code'] == 201
    assert 'status' in output
    assert isinstance(output['status'], str)
    assert output['status'] == 'OK'


def test_list_users(app, session):
    # Arrange
    client = app.test_client()

    # Act
    response = client.get('/api/v0.1/users')
    output = json.loads(response.get_data(as_text=True))

    # Assert
    assert 'code' in output
    assert isinstance(output['code'], int)
    assert output['code'] == 200
    assert 'status' in output
    assert output['status'] == 'OK'
