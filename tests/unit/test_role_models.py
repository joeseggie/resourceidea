from app.role.models.role import Role


def test_model_repr(session):
    """
    Test the value returned by the model's repr function.
    """
    # Arrange
    role_obj = Role(name='Administrator')

    # Act
    result = repr(role_obj)

    # Assert
    assert result == '<Role Administrator>'
