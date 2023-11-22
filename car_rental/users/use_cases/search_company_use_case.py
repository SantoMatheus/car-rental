from car_rental.users.models import Company


class SearchCompanyUseCase:

    def execute(self, cnpj: str):
        company = Company.objects.get(cnpj=cnpj)
        return company
