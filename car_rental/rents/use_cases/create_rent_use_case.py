import uuid

from car_rental.cars.models import Car
from car_rental.rents.exceptions.car_in_manutencion import CarInManutencion
from car_rental.rents.use_cases.calculate_total_price_use_case import CalculateTotalPriceUseCase
from car_rental.users.models import LegalRepresentative, Company
from car_rental.rents.exceptions.car_is_already_in_use import CarIsAlreadyInUse
from car_rental.rents.models import Rent


class LegalRepresentativeRentCreateUseCase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_toral_price_use_case = CalculateTotalPriceUseCase()

    def execute(self, user: str, days_amount: int, car_plate: str):
        car = Car.objects.get(car_plate=car_plate)
        if Car.status == "RENTED":
            raise CarIsAlreadyInUse()
        if Car.status == "IN_MANUTENCION":
            raise CarInManutencion()

        user = LegalRepresentative.objects.get(cpf=user)
        new_rent = Rent.objects.create(user=user, car_plate=car, days_amount=days_amount)
        new_rent.total_price = self.calculate_toral_price_use_case.execute(car_plate=car_plate)
        return new_rent


class CompanyRentCreateUseCase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_total_price_use_case = CalculateTotalPriceUseCase()

    def execute(self, user: str, days_amount: int, car_plate: str):
        car = Car.objects.get(car_plate=car_plate)
        if Car.status == "RENTED":
            raise CarIsAlreadyInUse()
        if Car.status == "IN_MANUTENCION":
            raise CarInManutencion()

        user = Company.objects.get(cnpj=user)
        new_rent = Rent.objects.create(user=user, car_plate=car, days_amount=days_amount)
        new_rent.total_price = self.calculate_total_price_use_case.execute(car_plate=car_plate)
        return new_rent


