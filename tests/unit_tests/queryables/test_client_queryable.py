"""Test client queryable.
"""
import unittest
from unittest.mock import Mock

from sqlalchemy.orm.query import Query

from app.queryables.client_queryable import ClientQueryable


class TestClientQueryable(unittest.TestCase):
    def test_to_list_returns_list(self):
        """Test to_list method returns a list.
        """
        queryable = ClientQueryable()
        result = queryable.to_list()
        self.assertIsInstance(result, list)

    def test_where_company_is_returns_Query(self):
        """Test where_company_is returns Query object.
        """
        queryable = ClientQueryable()
        comapny_id = Mock()
        result = queryable.where_company_is(comapny_id)
        self.assertIsInstance(result, Query)


if __name__ == '__main__':
    unittest.main()
