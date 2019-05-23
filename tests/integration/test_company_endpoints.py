from flask import json


def test_list_companies(app, session):
    # Arrange
    client = app.test_client()

    # Act
    resp = client.get('/api/v0.1/companies')
    response_output = json.loads(resp.get_data(as_text=True))

    # Assert
    assert 'code' in response_output
    assert 'data' in response_output
    assert 'status' in response_output
    assert isinstance(response_output['code'], int)
    assert response_output['status'] == 'OK'


def test_create_company(app, session):
    # Arrange
    client = app.test_client()

    # Act
    client_response = client.post('/api/v0.1/companies',
                                  json=dict(name='Test organization',
                                            address='Test address'))
    output = json.loads(client_response.get_data(as_text=True))

    # Assert
    assert 'code' in output
    assert isinstance(output['code'], int)
    assert output['code'] == 201
    assert 'status' in output
    assert output['status'] == 'OK'
    assert 'data' in output
