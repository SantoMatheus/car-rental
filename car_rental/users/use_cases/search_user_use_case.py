from car_rental.users.models import LegalRepresentative


class SearchLegalRepresentativeUseCase:
    def execute(self, cpf: str):
        legal_representative = LegalRepresentative.objects.filter(cpf=cpf)
        return legal_representative
