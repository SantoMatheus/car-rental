from rest_framework.exceptions import ValidationError


class CarNotAvailable(ValidationError):
    default_detail = 'Car not available for rent.'
    status_code = 409
