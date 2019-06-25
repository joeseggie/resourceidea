"""Unit tests app.resource.utils module"""
from app.employee.repository import EmployeeRepository
from app.organization.utils import get_organizations
from app.resource.models import Resource
from app.resource.utils import create_resource
from app.resource.utils import get_resource
from app.resource.utils import update_resource


def test_create_resource(session, fake_color):
    """Test create_resource function"""

    # Arrange
    org_list_params = {'sort_key': 'name', 'sort_order': 'asc'}
    fake_employee = next(iter(EmployeeRepository.get_all() or []), None)
    fake_organization = next(
        iter(get_organizations(**org_list_params) or []), None)
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


def test_update_resource(session, fake_color):
    """Test update_resource function."""

    # Arrange
    org_list_params = {'sort_key': 'name', 'sort_order': 'asc'}
    fake_employee = next(iter(EmployeeRepository.get_all() or []), None)
    fake_organization = next(
        iter(get_organizations(**org_list_params) or []), None)
    fake_resource = {
        'employee_id': fake_employee.id,
        'color': fake_color.hex_color(),
        'organization_id': fake_organization.id
    }
    fake_resource = create_resource(**fake_resource)
    original_color = fake_resource.color
    resource_updates = {'color': fake_color.hex_color()}

    # Act
    result = update_resource(fake_resource.id, **resource_updates)

    # Assert
    if not isinstance(result, Resource):
        raise AssertionError()
    if original_color == result.color:
        raise AssertionError()


def test_get_resource(session, fake_color):
    """Test get_resource function."""

    # Arrange
    org_list_params = {'sort_key': 'name', 'sort_order': 'asc'}
    fake_employee = next(iter(EmployeeRepository.get_all() or []), None)
    fake_organization = next(
        iter(get_organizations(**org_list_params) or []), None)
    fake_resource_input = {
        'employee_id': fake_employee.id,
        'color': fake_color.hex_color(),
        'organization_id': fake_organization.id
    }
    fake_resource = create_resource(**fake_resource_input)

    # Act
    result = get_resource(fake_resource.id)

    # Assert
    if not isinstance(result, Resource):
        raise AssertionError()
    if result.id != fake_resource.id:
        raise AssertionError()
