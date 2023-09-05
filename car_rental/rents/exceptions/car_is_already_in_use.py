from rest_framework.exceptions import ValidationError


class CarIsAlreadyInUse(ValidationError):
    default_detail = 'Car not available for rent. Already in use.'
    status_code = 409
