'''Department queryable unit tests.
'''
import unittest
from unittest.mock import Mock

from app.queryables.department_queryable import DepartmentQueryable


class TestDepartmentQueryable(unittest.TestCase):
    '''Test DepartmentQueryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method.
        '''
        queryable = DepartmentQueryable()
        result = queryable.to_list()
        self.assertIsInstance(result, list)

    def test_where_company_is_returns_DepartmentQueryable(self):
        '''Test where_company_is method returns DepartmentQueryable object.
        '''
        queryable = DepartmentQueryable()
        mock_company_id = Mock()
        result = queryable.where_company_is(mock_company_id)
        self.assertIsInstance(result, DepartmentQueryable)
