from rest_framework.exceptions import ValidationError


class CpfNumberAlreadyExists(ValidationError):
    default_detail = 'Cpf já cadastrado.'
    status_code = 409
