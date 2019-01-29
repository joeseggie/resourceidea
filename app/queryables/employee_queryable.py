'''Employee queryable.
'''
from datetime import datetime

from app.models.employee import Employee


class EmployeeQueryable:
    '''Employee queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.employee_queryable = Employee.query

    def is_terminated(self):
        '''Filter employees who are terminated.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.termination_date.isnot(None)
        )
        return self

    def is_not_terminated(self):
        '''Filter employees who are not terminated.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.termination_date.is_(None)
        )
        return self

    def where_company_is(self, company_id: int):
        '''Filter employees by company.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.user_account.has(company_id=company_id)
        )
        return self

    def joined_before(self, join_date: datetime):
        '''Filter employees who joined before a given date.

        Parameters
        ----------
        join_date {datetime} -- Date used to filter employees.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.join_date < join_date
        )
        return self

    def joined_after(self, join_date: datetime):
        '''Filter employees who joined after a given date.

        Parameters
        ----------
        join_date {datetime} -- Date used to filter employees.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.join_date > join_date
        )
        return self

    def terminated_before(self, termination_date: datetime):
        '''Filter employees who were terminated before a given date.

        Parameters
        ----------
        termination_date {datetime} -- Date used to filter employees.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.termination_date < termination_date
        )
        return self

    def terminated_after(self, termination_date: datetime):
        '''Filter employees who were terminated after a given date.

        Parameters
        ----------
        termination_date {datetime} -- Date used to filter employees.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.termination_date > termination_date
        )
        return self

    def to_list(self):
        '''List employees.
        '''
        query_result = self.employee_queryable.all()
        employees_list = [{
            'Id': result.id,
            'FileNumber': result.file_number,
            'FirstName': result.first_name,
            'LastName': result.last_name,
            'JoinDate': result.join_date,
            'TerminationDate': result.termination_date,
            'UserAccountId': result.user_account_id
        } for result in query_result]
        return employees_list

    def file_number_is(self, file_number: str):
        '''Filter employees by file number.

        Parameters
        ----------
        file_number {str} -- Employee file number.
        '''
        self.employee_queryable = self.employee_queryable.filter(
            Employee.file_number == file_number
        )
        return self
