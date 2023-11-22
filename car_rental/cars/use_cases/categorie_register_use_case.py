from car_rental.cars.exceptions.categorie_already_exists import CategorieAlreadyExists
from car_rental.cars.models import CarCategorie


class CategorieRegisterUseCase:

    def execute(self, categorie: str, value: float):

        categorie_queryset = CarCategorie.objects.filter(categorie=categorie)
        if categorie_queryset.exists() is True:
            raise CategorieAlreadyExists()

        new_categorie = CarCategorie.objects.create(categorie=categorie, value=value)
        return new_categorie
