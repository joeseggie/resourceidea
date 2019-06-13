"""Client Industry utils module"""
from app.client_industry.models import ClientIndustry
from app.client_industry.repositories import ClientIndustryRepository


def create_client_industry(name: str) -> ClientIndustry:
    """Creates client industry"""
    new_client_industry = ClientIndustry(name=name)
    return ClientIndustryRepository.add(new_client_industry)
