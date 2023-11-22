import uuid

from car_rental.cars.models import Car
from car_rental.rents.models import Rent


class CalculateTotalPriceUseCase:
    def execute(self, car: uuid, days_amount: int):
        car = Car.objects.get(id=car.id)
        rent_total_price = car.categorie.value * days_amount

        return rent_total_price
