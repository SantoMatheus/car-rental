from rest_framework.exceptions import ValidationError


class PaymentNotDone(ValidationError):
    default_detail = "PaymentCreateUseCase not done, insufficient funds."
    status_code = 400
