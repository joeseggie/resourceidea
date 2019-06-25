"""app.resource.utils module"""
from app.resource.models import Resource
from app.resource.repository import ResourceRepository


def create_resource(**kwargs):
    """Create a new resource"""
    new_resource = Resource(**kwargs)
    return ResourceRepository.create(new_resource)
