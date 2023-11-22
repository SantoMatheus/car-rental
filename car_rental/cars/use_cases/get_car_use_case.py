from car_rental.cars.models import Car


class GetCarUseCase:
    def execute(self, car_plate: str):
        car = Car.objects.filter(car_plate=car_plate)
        return car
