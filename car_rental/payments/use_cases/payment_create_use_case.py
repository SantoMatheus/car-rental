import uuid

from car_rental.charges.models import Charge
from car_rental.payments.exceptions.payment_alreay_done import PaymentAlreadyDone
from car_rental.payments.models import Payment


class PaymentCreateUseCase:
    def execute(self, charge: uuid):
        charge = Charge.objects.get(id=charge)
        if charge.rent.payment_status == "DONE":
            raise PaymentAlreadyDone()

        payment = Payment.objects.create(charge=charge)
        charge.rent.payment_status = "DONE"
        charge.save()

        return payment
