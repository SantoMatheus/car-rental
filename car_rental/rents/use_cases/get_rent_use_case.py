from car_rental.rents.models import Rent


class GetRentUseCase:
    def execute(self):
        rent = Rent.objects.filter()
        return rent
