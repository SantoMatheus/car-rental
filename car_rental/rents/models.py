import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem

from car_rental.cars.models import Car
from car_rental.users.models import LegalRepresentative


class Rent(TimeStampedModel):
    class PaymentStatusChoices(DjangoChoices):
        DONE = ChoiceItem('DONE')
        NOT_DONE = ChoiceItem('NOT_DONE')

    class PaymentMethodChoices(DjangoChoices):
        CREDIT_CARD = ChoiceItem("CREDIT_CARD")
        DEBIT_CARD = ChoiceItem("DEBIT_CARD")
        BILLET = ChoiceItem("BILLET")
        PIX = ChoiceItem("PIX")
        CASH = ChoiceItem("CASH")

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # criar atributo charge_number
    user = models.ForeignKey(LegalRepresentative, on_delete=models.CASCADE, related_name='client')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    days_amount = models.CharField(max_length=10)
    total_price = models.FloatField(default=0)
    payment_method = models.CharField(choices=PaymentMethodChoices, max_length=20)
    payment_status = models.CharField(choices=PaymentStatusChoices, default="NOT_DONE", max_length=20)


