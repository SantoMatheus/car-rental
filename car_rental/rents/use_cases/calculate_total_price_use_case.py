from car_rental.cars.models import Car
from car_rental.rents.models import Rent


class CalculateTotalPriceUseCase:
    def execute(self, car_plate):
        car = Car.objects.get(car_plate=car_plate)
        rent = Rent.objects.get(car_plate=car_plate)

        rent.total_price = car.categorie.value * rent.days_amount
        return rent.total_price
