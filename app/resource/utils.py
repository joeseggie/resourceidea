"""app.resource.utils module"""
from uuid import UUID

from app.resource.models import Resource
from app.resource.repository import ResourceRepository


def create_resource(**kwargs) -> Resource:
    """Create a new resource

    Returns:
        New resource.
    """
    new_resource = Resource(**kwargs)
    return ResourceRepository.create(new_resource)


def update_resource(resource_id: UUID, **kwargs) -> Resource:
    """
    Update a resource with the ID.

    Args:
        resource_id (UUID): ID of the resource to be updated.

    Returns:
        Updated resource.
    """
    update_fields = ('color', 'is_active', )
    return ResourceRepository.update_by_id(
        model_id=resource_id,
        fields_for_update=update_fields,
        **kwargs)
