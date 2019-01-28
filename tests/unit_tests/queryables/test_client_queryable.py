"""Test client queryable.
"""
from unittest.mock import Mock

from sqlalchemy.orm.query import Query

from app.queryables.client_queryable import ClientQueryable


def test_to_list_returns_list():
    """Test to_list method returns a list.
    """
    queryable = ClientQueryable()
    result = queryable.to_list()
    assert isinstance(result, list)


def test_where_company_is_returns_Query():
    """Test where_company_is returns Query object.
    """
    queryable = ClientQueryable()
    comapny_id = Mock()
    result = queryable.where_company_is(comapny_id)
    assert isinstance(result, Query)
