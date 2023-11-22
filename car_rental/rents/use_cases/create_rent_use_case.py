import uuid

from car_rental.cars.models import Car
from car_rental.rents.exceptions.car_in_manutencion import CarInMaintenance
from car_rental.rents.exceptions.car_is_already_in_use import CarIsAlreadyInUse
from car_rental.rents.models import Rent
from car_rental.rents.use_cases.calculate_total_price_use_case import CalculateTotalPriceUseCase
from car_rental.users.models import LegalRepresentative, Company


class LegalRepresentativeRentCreateUseCase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_total_price_use_case = CalculateTotalPriceUseCase()

    def execute(self, user: str, car: uuid,  days_amount: int, payment_method: str):
        car = Car.objects.get(id=car)
        if Car.status == "RENTED":
            raise CarIsAlreadyInUse()
        if Car.status == "IN_MAINTENANCE":
            raise CarInMaintenance()

        user_rent = LegalRepresentative.objects.get(cpf=user)
        car_rent = Car.objects.get(id=car.id)
        rent_total_price = self.calculate_total_price_use_case.execute(car=car_rent, days_amount=days_amount)

        new_rent = Rent.objects.create(user=user_rent, car=car_rent, days_amount=days_amount,
                                       payment_method=payment_method)
        new_rent.total_price = rent_total_price
        new_rent.save()
        return new_rent


class CompanyRentCreateUseCase:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_total_price_use_case = CalculateTotalPriceUseCase()

    def execute(self, user: str, days_amount: int, car_id: uuid):
        car = Car.objects.get(id=car_id)
        if Car.status == "RENTED":
            raise CarIsAlreadyInUse()
        if Car.status == "IN_MANUTENCION":
            raise CarInMaintenance()

        user_rent = Company.objects.get(cnpj=user)
        car_rent = Car.objects.get(id=car_id)
        rent_total_price = self.calculate_total_price_use_case.execute(car=car, days_amount=days_amount)

        new_rent = Rent.objects.create(user=user_rent, car_plate=car_rent, days_amount=days_amount)
        new_rent.total_price = rent_total_price
        new_rent.save()
        return new_rent


