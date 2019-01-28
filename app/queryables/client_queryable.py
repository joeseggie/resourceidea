"""Client queryable.
"""
from app.models.client import Client


class ClientQueryable:
    """Client queryable.
    """

    def __init__(self):
        """Constructor.
        """
        self.client_queryable = Client.query

    def to_list(self) -> list:
        """Get list of clients.
        """
        query_result = self.client_queryable.all()
        clients_list = [{
            'Id': result.id,
            'Name': result.name,
            'NameStub': result.name_stub,
            'Address': result.address,
            'CompanyId': result.company_id
        } for result in query_result]
        return clients_list

    def where_company_is(self, company_id: int):
        """Filter the clients by company.

        Parameters
        ----------
        company_id {int} -- Company Id.

        Returns
        -------
        ClientQueryable -- Client queryable.
        """
        self.client_queryable = self.client_queryable.filter_by(
            company_id=company_id
        )
        return self
