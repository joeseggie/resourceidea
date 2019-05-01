from app.company.repository import CompanyRepository


def get_companies_by_filter():
    CompanyRepository.filter_query()
