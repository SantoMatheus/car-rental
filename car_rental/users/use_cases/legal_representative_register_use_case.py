from car_rental.users.exceptions.cpf_number_already_exists import CpfNumberAlreadyExists
from ..models import LegalRepresentative


class LegalRepresentativeRegisterUseCase:

    def execute(self, name: str, birth_date: str, password: str, cpf: str, phone_number: str, zip_code: str,
                street_name: str, number: str, city: str, state: str, country: str):
        legal_representative_queryset = LegalRepresentative.objects.filter(cpf=cpf)
        if legal_representative_queryset.exists() is True:
            raise CpfNumberAlreadyExists()

        legal_representative = LegalRepresentative.objects.create(name=name, cpf=cpf, birth_date=birth_date,
                                                                  phone_number=phone_number, zip_code=zip_code,
                                                                  street_name=street_name, number=number, city=city,
                                                                  state=state, country=country, username=cpf)
        legal_representative.set_password(raw_password=password)
        legal_representative.save()
        return legal_representative
