import json

import pytest

from app import create_app, db


@pytest.fixture
def client():
    app = create_app('testing')
    client = app.test_client()
    with app.app_context() as app_context:
        app_context.push()
        db.init_app(app)
        print(app.config)
        db.create_all()

        yield client

        db.session.remove()
        db.drop_all()
        app_context.pop()


class TestServicePlanRoutes:
    '''
    ServicePlans test suite.
    '''

    def test_base_route(self, client):
        '''
        Test the base route response.
        '''

        # Act
        rv = client.get('/api/v1/serviceplans')
        data = json.loads(rv.get_data(as_text=True))

        # Assert
        assert rv.status_code == 200
        assert data['status'] == 'OK'
