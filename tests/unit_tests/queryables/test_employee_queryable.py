'''Test employee queryable.
'''
from datetime import datetime
from unittest.mock import Mock

from app.queryables.employee_queryable import EmployeeQueryable


class TestEmployeeQueryable:
    '''Test employee queryable.
    '''
    def test_to_list_returns_list(self):
        '''Test to_list method returns list.
        '''
        queryable = EmployeeQueryable()
        result = queryable.to_list()
        assert isinstance(result, list)

    def test_where_company_is_returns_EmployeeQueryable(self):
        '''Test where_company_is returns EmployeeQueryable object.
        '''
        queryable = EmployeeQueryable()
        mock_company_id = Mock()
        result = queryable.where_company_is(mock_company_id)
        assert isinstance(result, EmployeeQueryable)

    def test_joined_before_returns_EmployeeQueryable(self):
        '''Test joined_before returns EmployeeQueryable.
        '''
        queryable = EmployeeQueryable()
        filter_date = datetime.now()
        result = queryable.joined_before(filter_date)
        assert isinstance(result, EmployeeQueryable)

    def test_joined_after_returns_EmployeeQueryable(self):
        '''Test joined_after returns EmployeeQueryable.
        '''
        queryable = EmployeeQueryable()
        filter_date = datetime.now()
        result = queryable.joined_after(filter_date)
        assert isinstance(result, EmployeeQueryable)

    def test_is_terminated_returns_EmployeeQueryable(self):
        '''Test is_terminated returns EmployeeQueryable object.
        '''
        queryable = EmployeeQueryable()
        result = queryable.is_terminated()
        assert isinstance(result, EmployeeQueryable)

    def test_is_not_terminated_returns_EmployeeQueryable(self):
        '''Test is_not_terminated returns EmployeeQueryable object.
        '''
        queryable = EmployeeQueryable()
        result = queryable.is_not_terminated()
        assert isinstance(result, EmployeeQueryable)

    def test_terminated_before_returns_EmployeeQueryable(self):
        '''Test terminated_before returns EmployeeQueryable.
        '''
        queryable = EmployeeQueryable()
        filter_date = datetime.now()
        result = queryable.terminated_before(filter_date)
        assert isinstance(result, EmployeeQueryable)

    def test_terminated_after_returns_EmployeeQueryable(self):
        '''Test terminated_after returns EmployeeQueryable.
        '''
        queryable = EmployeeQueryable()
        filter_date = datetime.now()
        result = queryable.terminated_after(filter_date)
        assert isinstance(result, EmployeeQueryable)

    def test_file_number_is_returns_EmployeeQueryable(self):
        '''Test file_number_is returns EmployeeQueryable.
        '''
        queryable = EmployeeQueryable()
        mock_file_number = Mock()
        result = queryable.file_number_is(mock_file_number)
        assert isinstance(result, EmployeeQueryable)
