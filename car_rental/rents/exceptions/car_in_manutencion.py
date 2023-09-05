from rest_framework.exceptions import ValidationError


class CarInManutencion(ValidationError):
    default_detail = "Car not available. In manutencion."
    status_code = 409