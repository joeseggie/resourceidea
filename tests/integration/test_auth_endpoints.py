from flask import json


def test_signup(app, session):
    # Arrange
    client = app.test_client()

    # Act
    client_response = client.post('/api/v0.1/signup',
                                  json=dict(organization='Test organization'))
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert client_response.status_code == 201
    assert 'status' in output
    assert output['status'] == 'OK'
    assert 'data' in output
