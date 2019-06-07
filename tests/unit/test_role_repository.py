from app.role.models.role import Role
from app.role.repositories.role_repository import RoleRepository


def test_update(session):
    """
    Test the role repository update function.
    """
    # Arrange
    test_model = RoleRepository.create(Role(name='Super User'))
    test_model_id = test_model.id
    update_fields = ('name',)

    # Act
    result = RoleRepository.update(test_model_id, update_fields, name='Admin User')

    # Assert
    assert isinstance(result, Role)
    assert result.normalized_name == 'admin-user'
    assert result.name == 'Admin User'


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
    role_name = 'Super User'
    normalized_role_name = 'super-user'
    RoleRepository.create(
        Role(name=role_name, normalized_name=normalized_role_name))


    # Act
    result = RoleRepository.get_by_name(role_name)

    # Assert
    assert isinstance(result, Role)
    assert result.name == role_name
    assert result.normalized_name == normalized_role_name


def test_create(session):
    """
    Test role repository create function.
    """
    # Arrange
    role_name = 'Super User'
    normalized_role_name = 'super-user'

    # Act
    result = RoleRepository.create(
        Role(name=role_name, normalized_name=normalized_role_name))

    # Assert
    assert isinstance(result, Role)
    assert result.name == role_name
    assert result.normalized_name == normalized_role_name


def test_update_by_id(session):
    """
    Test role repository update_by_id function.
    """
    # Arrange
    role_name = 'New Role'
    normalized_role_name = 'new-role'
    test_stub = RoleRepository.create(
        Role(name=role_name, normalized_name=normalized_role_name))
    update_fields = ('name', 'normalized_name')
    role_update = 'Role update'
    normalized_role_update = 'role-update'

    # Act
    result = RoleRepository.update_by_id(
        model_id=test_stub.id,
        fields_for_update=update_fields,
        name=role_update,
        normalized_name=normalized_role_update
    )

    # Assert
    assert isinstance(result, Role)
    assert result.normalized_name == normalized_role_update
    assert result.name == role_update
