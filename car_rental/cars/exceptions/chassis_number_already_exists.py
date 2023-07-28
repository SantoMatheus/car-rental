from rest_framework.exceptions import ValidationError


class ChassisNumberAlreadyExists(ValidationError):
    default_detail = 'Chassis já cadastrado'
    status_code = 409

