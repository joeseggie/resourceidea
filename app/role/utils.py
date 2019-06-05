from uuid import UUID

from app.role.models import Role
from app.role.repositories import RoleRepository


def create_role(role_name: str):
    new_role = Role(name=role_name)
    return RoleRepository.create(new_role)


def list_roles():
    return RoleRepository.get_all()


def get_role(role_id: str):
    return RoleRepository.get_one_by_id(UUID(role_id))
