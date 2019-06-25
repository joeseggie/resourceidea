"""Unit tests app.resource.utils module"""
from app.employee.repository import EmployeeRepository
from app.organization.utils import get_organizations
from app.resource.models import Resource
from app.resource.utils import create_resource


def test_create_resource(session, fake_color):
    """Test create_resource function"""

    # Arrange
    org_list_params = {'sort_key': 'name', 'sort_order': 'asc'}
    fake_employee = next(iter(EmployeeRepository.get_all() or []), None)
    fake_organization = next(iter(get_organizations(**org_list_params) or []), None)
    fake_resource = {
        'employee_id': fake_employee.id,
        'color': fake_color.hex_color(),
        'organization_id': fake_organization.id
    }

    # Act
    result = create_resource(**fake_resource)

    # Assert
    if not isinstance(result, Resource):
        raise AssertionError()
