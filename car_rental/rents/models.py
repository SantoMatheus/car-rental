import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem

from car_rental.cars.models import Car
from car_rental.user.models import User


class Rent(TimeStampedModel):
    class PaymentStatusChoices(DjangoChoices):
        DONE = ChoiceItem('DONE')
        NOT_DONE = ChoiceItem('NOT_DONE')

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=10)
    end_date = models.DateTimeField(max_length=10)
    total_price = models.FloatField(default=0)
    payment_status = models.CharField(choices=PaymentStatusChoices, default="NOT_DONE")


