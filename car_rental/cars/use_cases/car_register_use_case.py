from car_rental.cars.models import Car


class CarRegisterUseCase:
    def execute(self, manufacturer: str, categorie: str, manufacture_year: int, model_year: int, mileage: float,
                color: str, fuel_type: str, fuel_level: str, chassis_number: str):
        car = Car.objects.create(chassis_number=chassis_number, manufacturer=manufacturer, categorie=categorie,
                                 manufacture_year=manufacture_year, model_year=model_year, mileage=mileage, color=color,
                                 fuel_type=fuel_type, fuel_level=fuel_level)
        return car
