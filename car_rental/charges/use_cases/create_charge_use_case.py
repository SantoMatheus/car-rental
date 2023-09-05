import uuid

from car_rental.charges.exceptions.charge_already_exists import ChargeAlreadyExists
from car_rental.payments.exceptions.payment_is_alreay_done import PaymentIsAlreadyDone
from car_rental.charges.models import Charge
from car_rental.rents.models import Rent


class ChargeUseCase:
    def execute(self, rent_id: uuid, payment_method: str):
        charge_informations = Charge.objects.filter(id=rent_id)
        if charge_informations.id.exist() is True:
            raise ChargeAlreadyExists()

        if charge_informations.status == "DONE":
            raise PaymentIsAlreadyDone()

        rent = Rent.objects.get(id=rent_id)
        rent.payment_method = payment_method
        charge = Charge.objects.create(id=rent, payment_method=payment_method)
        return charge
