import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem


class CarCategorie(TimeStampedModel):

    class CarCategorieChoices(DjangoChoices):
        COMPACT_CAR = ChoiceItem("COMPACT_CAR")
        COMPACT_PREMIUM = ChoiceItem("COMPACT_PREMIUM")
        SMALL_SEDAN = ChoiceItem("SEDAN")
        SEDAN = ChoiceItem("SEDAN")
        SPORTS_CAR = ChoiceItem("SPORTS_CAR")
        SUV = ChoiceItem("SUV")
        LIGHTWEIGTH_TRUCK = ChoiceItem("LIGHTWEIGTH_TRUCK")
        HEAVY_DUTY_TRUCK = ChoiceItem("HEAVY_DUTY_TRUCK")
        FAMILY_VAN = ChoiceItem("FAMILY_VAN")
        WORK_VAN = ChoiceItem("WORK_VAN")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    categorie = models.CharField(choices=CarCategorieChoices, max_length=30, unique=True)
    value = models.FloatField()


class Car(TimeStampedModel):

    class CarStatusChoices(DjangoChoices):
        AVAILABLE = ChoiceItem("AVAILABLE")
        RENTED = ChoiceItem("RENTED")
        IN_MAINTENANCE = ChoiceItem("IN_MAINTENANCE")

    class FuelTypeChoices(DjangoChoices):
        GASOLINE = ChoiceItem("GASOLINE")
        ETHANOL = ChoiceItem("ETHANOL")
        DIESEL = ChoiceItem("DIESEL")
        ELECTRIC_VEHICLE = ChoiceItem("ELECTRIC_VEHICLE")

    class FuelLevelChoices(DjangoChoices):
        EMPTY = ChoiceItem("EMPTY")
        FULL = ChoiceItem("FULL")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # criar atributo Car_name e AT/MT
    chassis_number = models.CharField(max_length=17, unique=True)
    manufacturer = models.CharField(max_length=50)
    categorie = models.ForeignKey(CarCategorie, on_delete=models.CASCADE)
    manufacture_year = models.DateTimeField()
    model_year = models.DateTimeField()
    mileage = models.FloatField()
    car_plate = models.CharField(max_length=7, unique=True)
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(choices=FuelTypeChoices, max_length=30)
    fuel_level = models.CharField(choices=FuelLevelChoices, max_length=30)
    status = models.CharField(default="AVAILABLE", max_length=13)
