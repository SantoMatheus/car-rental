from car_rental.users.exceptions.cnpj_number_already_exists import CnpjNumberAlreadyExists
from car_rental.users.models import Company, LegalRepresentative


class CompanyRegisterUseCase:

    def execute(self, legal_representative: str, register_name:str, company_name: str, cnpj: str, phone_number: str,
                zip_code: str, street_name: str, number: str, city: str, state: str, country: str):
        company_queryset = Company.objects.filter(cnpj=cnpj)
        if company_queryset.exists() is True:
            raise CnpjNumberAlreadyExists()

        legal_representative_informations = LegalRepresentative.objects.get(cpf=legal_representative)
        company = Company.objects.create(legal_representative=legal_representative_informations,
                                         company_name=company_name, register_name=register_name,
                                         cnpj=cnpj, phone_number=phone_number, zip_code=zip_code,
                                         street_name=street_name, number=number, city=city, state=state, country=country)
        return company
