from app.common.base_repository import BaseRepository
from app.role.models.user_role import UserRole


class UserRoleRepository(BaseRepository):
    """
    User role repository.
    """
    model_class = UserRole
