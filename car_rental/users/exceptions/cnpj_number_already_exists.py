from rest_framework.exceptions import ValidationError


class CnpjNumberAlreadyExists(ValidationError):
    default_detail = "O CNPJ informado já está cadastrado."
    status_code = 409
