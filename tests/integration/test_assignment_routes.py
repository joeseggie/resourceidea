from datetime import datetime
import json

from app.models.assignment import Assignment
from database import db


class TestAssignmentRoutes:
    '''
    Test suite for the assignment routes.
    '''
    def test_listing_assignments_api_response(self, client):
        '''
        Test the response returned by the API when listing assignments.
        '''
        # Act
        response = client.get('/api/v1/assignments')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert isinstance(response_data['data'], list)

    def test_adding_assignment_api_response(self, client):
        '''
        Test the response returned by the API when adding a new assignment.
        '''
        # Arrange
        request_data = {
            'starts': '2019-01-12 08:00:00',
            'ends': '2019-09-30 17:00:00'
        }

        # Act
        response = client.post('/api/v1/assignments', data=request_data)
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 201
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 201
        assert response_data['data']['starts'] == '2019-01-12 08:00:00'
        assert response_data['data']['ends'] == '2019-09-30 17:00:00'

    def test_assignment_query_api_response(self, client):
        '''
        Test response returned when querying for an assignment.
        '''
        # Arrange
        start_date = datetime(2019, 1, 10, 8, 0, 0)
        end_date = datetime(2019, 9, 30, 17, 0, 0)
        assignment = Assignment(
            starts=start_date,
            ends=end_date
        )
        db.session.add(assignment)
        db.session.commit()

        # Act
        response = client.get('/api/v1/assignments/1')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['starts'] == '2019-01-10 08:00:00'
        assert response_data['data']['ends'] == '2019-09-30 17:00:00'

    def test_assignment_update_api_response(self, client):
        '''
        Test the response returned by API when updating an assignment.
        '''
        # Arrange
        start_date = datetime(2019, 1, 10, 8, 0, 0)
        end_date = datetime(2019, 9, 30, 17, 0, 0)
        assignment = Assignment(
            starts=start_date,
            ends=end_date
        )
        db.session.add(assignment)
        db.session.commit()

        request_data = {
            'id': 1,
            'starts': '2019-01-28 08:00:00',
            'ends': '2019-09-10 17:00:00'
        }

        # Act
        response = client.put('/api/v1/assignments/1', data=request_data)
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['starts'] == '2019-01-28 08:00:00'
        assert response_data['data']['ends'] == '2019-09-10 17:00:00'

    def test_assignment_start_date_update_api_response(self, client):
        '''
        Test the response returned by API when updating an assignment.
        '''
        # Arrange
        start_date = datetime(2019, 1, 10, 8, 0, 0)
        end_date = datetime(2019, 9, 30, 17, 0, 0)
        assignment = Assignment(
            starts=start_date,
            ends=end_date
        )
        db.session.add(assignment)
        db.session.commit()

        request_data = {
            'id': 1,
            'starts': '2019-01-28 08:00:00',
        }

        # Act
        response = client.patch('/api/v1/assignments/1', data=request_data)
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        print(response_data)
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['starts'] == '2019-01-28 08:00:00'
        assert response_data['data']['ends'] == '2019-09-30 17:00:00'

    def test_assignment_end_date_update_api_response(self, client):
        '''
        Test the response returned by API when updating an assignment.
        '''
        # Arrange
        start_date = datetime(2019, 1, 10, 8, 0, 0)
        end_date = datetime(2019, 9, 30, 17, 0, 0)
        assignment = Assignment(
            starts=start_date,
            ends=end_date
        )
        db.session.add(assignment)
        db.session.commit()

        request_data = {
            'id': 1,
            'ends': '2019-09-18 17:00:00',
        }

        # Act
        response = client.patch('/api/v1/assignments/1', data=request_data)
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        print(response_data)
        assert response.status_code == 200
        assert response_data['status'] == 'OK'
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1
        assert response_data['data']['starts'] == '2019-01-10 08:00:00'
        assert response_data['data']['ends'] == '2019-09-18 17:00:00'

    def test_response_code_when_assignment_not_found(self, client):
        # Act
        response = client.get('/api/v1/assignments/99999')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 404
        assert response_data['code'] == 404

    def test_response_code_when_assignment_update_not_found(self, client):
        # Act
        response = client.put('/api/v1/assignments/99999')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 404
        assert response_data['code'] == 404

    def test_assignment_patch_response_code_when_not_found(self, client):
        # Act
        response = client.patch('/api/v1/assignments/99999')
        response_data = json.loads(response.get_data(as_text=True))

        # Assert
        assert response.status_code == 404
        assert response_data['code'] == 404
