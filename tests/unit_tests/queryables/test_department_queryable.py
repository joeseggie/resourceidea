'''Department queryable unit tests.
'''
from unittest.mock import Mock

from app.queryables.department_queryable import DepartmentQueryable


class TestDepartmentQueryable:
    '''Test DepartmentQueryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method.
        '''
        queryable = DepartmentQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_DepartmentQueryable(self):
        '''Test where_company_is method returns DepartmentQueryable object.
        '''
        queryable = DepartmentQueryable()
        mock_company_id = Mock()
        result = queryable.where_company_is(mock_company_id)
        assert isinstance(result, DepartmentQueryable)
