import uuid

from car_rental.cars.exceptions.chassis_number_already_exists import ChassisNumberAlreadyExists
from car_rental.cars.models import Car, CarCategorie


class CarRegisterUseCase:
    def execute(self, manufacturer: str, categorie: str, manufacture_year: int, model_year: int, mileage: float,
                car_plate: str, color: str, fuel_type: str, fuel_level: str, chassis_number: str):
        car_queryset = Car.objects.filter(chassis_number=chassis_number)
        if car_queryset.exists() is True:
            raise ChassisNumberAlreadyExists()

        categorie = CarCategorie.objects.get(categorie=categorie)

        car = Car.objects.create(chassis_number=chassis_number, manufacturer=manufacturer, categorie=categorie,
                                 manufacture_year=manufacture_year, model_year=model_year, mileage=mileage,
                                 car_plate=car_plate, color=color, fuel_type=fuel_type, fuel_level=fuel_level)
        return car
