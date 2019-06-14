"""Test the client industry endpoints"""
from uuid import UUID

from flask import json


def test_post_client_industry(app, session, fake_lorem):
    # Arrange
    client = app.test_client()
    request_body = {
        "name": fake_lorem.word()
    }

    # Act
    result = client.post(
        '/api/v0.1/clientindustries',
        json=request_body)
    output = json.loads(result.get_data(as_text=True))

    # Assert
    assert result.status_code == 201
    assert 'id' in output
    assert 'name' in output
    assert isinstance(output, dict)
    assert isinstance(UUID(output['id']), UUID)


def test_post_client_industry_exists(app, session, fake_lorem):
    """Test response when the client industry name exists."""
    # Arrange
    client = app.test_client()
    request_body = {
        'name': 'Existing name'
    }

    # Act
    result = client.post(
        '/api/v0.1/clientindustries',
        json=request_body)
    output = json.loads(result.get_data(as_text=True))

    # Assert
    assert result == 400
    assert 'message' in output
