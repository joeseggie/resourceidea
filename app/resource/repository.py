"""app.resource.repository module"""
from app.common.base_repository import BaseRepository
from app.resource.models import Resource


class ResourceRepository(BaseRepository):
    """Resource repository"""
    model_class = Resource
