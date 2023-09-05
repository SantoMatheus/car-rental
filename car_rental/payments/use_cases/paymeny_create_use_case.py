import uuid

from car_rental.charges.models import Charge
from car_rental.payments.exceptions.payment_is_alreay_done import PaymentIsAlreadyDone
from car_rental.payments.exceptions.payment_not_done import PaymentNotDone
from car_rental.payments.models import Payment


class Payment:
    def execute(self, charge_id: uuid, value: float):
        charge_informations = Charge.objects.get(charge=charge_id)
        if charge_informations.payment_status == "DONE":
            raise PaymentIsAlreadyDone()

        if charge_informations.total_price != value:
            raise PaymentNotDone()

        charge_informations.payment_status = "DONE"
        charge_informations.save()
        payment = Payment.objects.create(charge=charge_id)
        return payment
