import uuid
from uuid import uuid4

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Car(TimeStampedModel):
    fuel_type_choices = (
        ("G", "Gasoline"),
        ("E", "Ethanol"),
        ("D", "Diesel"),
        ("EV", "Electric Vehicle")
    )

    fuel_level_choices = (
        ("E", "Empty"),
        ("F", "Full")
    )

    car_categorie_choices = (
        ("CC", "Compact Car"),
        ("CP", "Compacte Premium"),
        ("SC", "Sedan Coupe"),
        ("SP", "Sport Car"),
        ("SUV", "Sport Utility Vehicle"),
        ("LT", "Light Truck"),
        ("HDT", "Heavy Duty Truck"),
        ("FV", "Family Van"),
        ("WV", "Work Van"),
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    chassis_number = models.CharField(max_length=17)
    manufacturer = models.CharField(max_length=50)
    categorie = models.CharField(choices=car_categorie_choices, max_length=255)
    manufacture_year = models.DateTimeField()
    model_year = models.DateTimeField()
    mileage = models.FloatField()
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(choices=fuel_type_choices, max_length=255)
    fuel_level = models.CharField(choices=fuel_level_choices, max_length=255)


