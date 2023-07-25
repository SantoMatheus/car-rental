import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel, AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateTimeField()

    USERNAME_FIELD = 'cpf'
