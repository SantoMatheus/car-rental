import uuid

from car_rental.cars.models import Car
from car_rental.user.models import User
from car_rental.rents.exceptions.car_not_available import CarNotAvailable
from car_rental.rents.models import Rent


class RentCreateUseCase:
    def execute(self, user: str, start_date: str, end_date: str, car_plate: str):
        car = Car.objects.get(car_plate=car_plate)
        if Car.status == "RENTED":
            raise CarNotAvailable()

        user = User.objects.get(cpf=user)

        car = Car.id
        user = User.cpf

        new_rent = Rent.objects.create(user=user, id_car=car, start=start_date, end=end_date)
        return new_rent
