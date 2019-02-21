'''Department queryable.
'''
from ..models.department import Department


class DepartmentQueryable:
    '''Department queryable.
    '''
    def __init__(self):
        '''Constructor.
        '''
        self.department_queryable = Department.query

    def to_list(self):
        '''Get departments list.
        '''
        query_result = self.department_queryable.all()
        departments_list = [{
            'Id': result.id,
            'Name': result.name,
            'CompanyId': result.company_id
        } for result in query_result]
        return departments_list

    def where_company_is(self, company_id: int):
        '''Filter departments by company.

        Parameters
        ----------
        company_id {int} -- Company Id.
        '''
        self.department_queryable = self.department_queryable.filter_by(
            company_id=company_id
        )
        return self
