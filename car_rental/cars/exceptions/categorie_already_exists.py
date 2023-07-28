from rest_framework.exceptions import ValidationError


class CategorieAlreadyExists(ValidationError):
    default_detail = 'A categoria informada já existe.'
    status_code = 409
