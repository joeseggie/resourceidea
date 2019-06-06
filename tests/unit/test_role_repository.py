from app.role.models.role import Role
from app.role.repositories.role_repository import RoleRepository


def test_update(session):
    """
    Test the role repository update function.
    """
    # Arrange
    test_model_id = RoleRepository.get_all(
        sort_key='name',
        sort_order='asc'
    )[0].id
    update_fields = ('name',)

    # Act
    result = RoleRepository.update(test_model_id, update_fields, name='Super User')

    # Assert
    assert isinstance(result, Role)
    assert result.normalized_name == 'super-user'
    assert result.name == 'Super User'


def test_get_all(session):
    """
    Test role repository get_all function
    """
    # Arrange
    sort_key = 'name'
    sort_order = 'asc'

    # Act
    result = RoleRepository.get_all(sort_key=sort_key, sort_order=sort_order)

    # Assert
    assert isinstance(result, list)


def test_get_by_name(session):
    """
    Test role repository get_by_name function.
    """
    # Arrange
    role_name = 'Administrator'
    normalized_role_name = 'administrator'

    # Act
    result = RoleRepository.get_by_name(role_name)

    # Assert
    assert isinstance(result, Role)
    assert result.name == role_name
    assert result.normalized_name == normalized_role_name
