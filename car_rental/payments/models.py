import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel

from car_rental.charges.models import Charge


class Payment(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    charge = models.ForeignKey(Charge, on_delete=models.CASCADE)
