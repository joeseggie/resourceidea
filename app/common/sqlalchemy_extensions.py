from uuid import UUID

from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import Query


class CustomBaseQuery(BaseQuery):
    def to_list(self) -> list:
        return self.all()

    def where_company_is(self, company_id: UUID) -> Query:
        return self.filter_by(company_id=company_id)
