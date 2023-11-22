import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from django_extensions.db.models import TimeStampedModel


class LegalRepresentative(TimeStampedModel, AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, primary_key=True)
    birth_date = models.DateTimeField()
    phone_number = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=8)
    street_name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    password = models.CharField(max_length=12)


class Company(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    legal_representative = models.ForeignKey(LegalRepresentative, on_delete=CASCADE,
                                             related_name="companies")
    register_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, primary_key=True)
    phone_number = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=8)
    street_name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    country = models.CharField(max_length=55)

