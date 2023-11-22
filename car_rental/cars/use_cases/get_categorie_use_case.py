from car_rental.cars.models import CarCategorie


class GetCategorieUseCase:
    def execute(self):
        car_categorie = CarCategorie.objects.filter()
        return car_categorie
