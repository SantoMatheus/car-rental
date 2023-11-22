import uuid

from car_rental.charges.exceptions.charge_already_exists import ChargeAlreadyExists
from car_rental.payments.exceptions.payment_alreay_done import PaymentAlreadyDone
from car_rental.charges.models import Charge
from car_rental.rents.models import Rent


class ChargeUseCase:
    def execute(self, rent_id: uuid):
        rent = Rent.objects.get(id=rent_id)
        charge = Charge.objects.create(rent=rent)
        return charge
