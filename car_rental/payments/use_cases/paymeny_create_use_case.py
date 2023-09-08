import uuid

from car_rental.charges.models import Charge
from car_rental.payments.exceptions.payment_is_alreay_done import PaymentIsAlreadyDone
from car_rental.payments.models import Payment


class PaymentCreateUseCase:
    def execute(self, charge_id: uuid):
        charge_informations = Charge.objects.get(charge=charge_id)
        if charge_informations.payment_status == "DONE":
            raise PaymentIsAlreadyDone()

        charge_informations.payment_status = "DONE"
        charge_informations.save()
        payment = PaymentCreateUseCase.objects.create(charge=charge_id)
        return payment
