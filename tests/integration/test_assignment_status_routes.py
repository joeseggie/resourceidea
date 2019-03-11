import json

from app.models.assignment_status import AssignmentStatus
from database import db


class TestAssignmentStatusRoutes:
    '''
    AssignmentStatus routes test suite
    '''
    def test_assignment_status_GET_route_response(self, client):
        '''
        Test the response returned by the assignment status list route.
        '''
        # Act
        response = client.get('/api/v1/assignmentstatuses')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert isinstance(response_data['data'], list)
        assert response_data['code'] == 200

    def test_assignment_status_POST_route_response(self, client):
        '''
        Test response returned by API when adding an assignment status.
        '''
        # Arrange
        request_data = {
            'description': 'Test assignment status'
        }

        # Act
        response = client.post('/api/v1/assignmentstatuses', data=request_data)
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 201
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 201

    def test_assignment_status_query_response(self, client):
        '''
        Test response returned by API when querying for an assignment status.
        '''
        # Arrange
        mock_assignment_status = AssignmentStatus(description='Mocking')
        db.session.add(mock_assignment_status)
        db.session.commit()

        # Act
        response = client.get('/api/v1/assignmentstatuses/1')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['description'] == 'Mocking'

    def test_assignment_status_update_api_response(self, client):
        '''
        Test the response returned by API when updating an assignment status.
        '''
        # Arrange
        mock_assignment_status = AssignmentStatus(description='Mocking')
        db.session.add(mock_assignment_status)
        db.session.commit()
        request_data = {
            'description': 'Mocked update'
        }

        # Act
        response = client.put(
            '/api/v1/assignmentstatuses/1', data=request_data
        )
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['description'] == 'Mocked update'
