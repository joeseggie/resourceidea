from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime
from uuid import UUID

from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import Query


class CustomBaseQuery(BaseQuery):
    def to_list(self) -> list:
        return self.all()

    def where_company_is(self, company_id: UUID) -> Query:
        return self.filter_by(company_id=company_id)


class utcnow(expression.FunctionElement):
    type = DateTime()


@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
