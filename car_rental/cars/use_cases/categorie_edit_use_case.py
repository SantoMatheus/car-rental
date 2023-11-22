import uuid

from car_rental.cars.models import CarCategorie


class CategorieEditUseCase:
    def execute(self, id_categorie: uuid, categorie_name: str, new_value: float):
        categorie = CarCategorie.objects.get(id=id_categorie)
        categorie.value = new_value
        categorie.categorie = categorie_name
        categorie.save()
        return categorie




