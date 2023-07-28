import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel
from djchoices import DjangoChoices, ChoiceItem


class User(TimeStampedModel, AbstractUser):

    class UserTypeChoices(DjangoChoices):
        CPF = ChoiceItem("CPF")
        CNPJ = ChoiceItem("CNPJ")

    id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    cnpj = models.CharField(max_length=14)
    birth_date = models.DateTimeField()
    type = models.CharField(max_length=4, choices=UserTypeChoices)

    USERNAME_FIELD = 'cpf' or 'cnpj'
