import json


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
