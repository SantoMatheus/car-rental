from rest_framework.exceptions import ValidationError


class ChargeAlreadyExists(ValidationError):
    default_detail = "Already exists a charge vinculated to this users."
