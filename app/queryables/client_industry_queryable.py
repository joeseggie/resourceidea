"""Client industry queryable.
"""
from sqlalchemy.orm.query import Query

from app.models.client_industry import ClientIndustry


class ClientIndustryQueryable:
    """Client industry queryable.
    """

    def __init__(self):
        """Constructor.
        """
        self.client_industry_queryable = ClientIndustry.query

    def to_list(self):
        """Get a list of client industries.
        """
        query_result = self.client_industry_queryable.all()
        client_industries_list = [{
            'Id': result.id,
            'Name': result.name,
            'CompanyId': result.company_id
        } for result in query_result]
        return client_industries_list

    def where_company_is(self, company_id: int) -> Query:
        """Filter client industries by company.

        Parameters
        ----------
        company_id {int} -- Company Id.

        Returns
        -------
        Query -- sqlalchemy.orm.query.Query object.
        """
        self.client_industry_queryable = self.client_industry_queryable.filter_by(
            company_id=company_id
        )
        return self
