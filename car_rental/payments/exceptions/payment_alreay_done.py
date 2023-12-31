from rest_framework.exceptions import ValidationError


class PaymentAlreadyDone(ValidationError):
    default_detail = "The payment mentioned is already done."
    status_code = 409