import json

from app import db
from app.models.service_plan import ServicePlan


class TestServicePlanRoutes:
    '''
    ServicePlans test suite.
    '''

    def test_service_plans_GET_route_response(self, client):
        '''
        Test the service plans GET route response.
        '''

        # Act
        rv = client.get('/api/v1/serviceplans')
        data = json.loads(rv.get_data(as_text=True))

        # Assert
        assert rv.status_code == 200
        assert data['status'] == 'OK'

    def test_service_plans_POST_route_response(self, client):
        '''
        Test the service plans POST route response.
        '''
        # Arrange
        request_data = {
            'name': 'Test service plan',
            'price': 123.0
        }

        # Act
        response = client.post('/api/v1/serviceplans', data=request_data)
        data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 201
        assert data['status'] == 'OK'

    def test_service_plan_query_GET_route_response(self, client):
        '''
        Test the response returned when querying for a service plan by Id.
        '''
        # Arrange
        service_plan = ServicePlan(name='Query for plan', price=50.0)
        db.session.add(service_plan)
        db.session.commit()

        # Act
        response = client.get('/api/v1/serviceplans/1')
        data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert data['status'] == 'OK'
        assert data['data']['id'] == 1
        assert data['data']['name'] == 'Query for plan'
        assert data['data']['price'] == 50.0

    def test_service_plan_update_PUT_route_responses(self, client):
        '''
        Test the response returned when updating a service plan
        '''
        # Arrange
        service_plan = ServicePlan(name='Plan for update', price=50.0)
        db.session.add(service_plan)
        db.session.commit()

        request_data = {
            'name': 'Updated plan',
            'price': 100.0
        }

        # Act
        response = client.put('/api/v1/serviceplans/1', data=request_data)
        data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert data['status'] == 'OK'
        assert data['data']['id'] == 1
        assert data['data']['name'] == 'Updated plan'
        assert data['data']['price'] == 100.0
