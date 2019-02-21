"""Companies queryable.
"""
from ..models.company import Company


class CompanyQueryable:
    """Query companies
    """

    def __init__(self):
        """Constructor.
        """
        self.company_queryable = Company.query

    def to_list(self):
        """List companies.
        """
        query_result = self.company_queryable.all()
        companies_list = [{
            'Id': result.id,
            'Name': result.name,
            'NameStub': result.name_stub,
            'Address': result.address
        } for result in query_result]
        return companies_list
