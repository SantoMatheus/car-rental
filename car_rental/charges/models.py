import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel

from car_rental.rents.models import Rent


class Charge(TimeStampedModel):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)



