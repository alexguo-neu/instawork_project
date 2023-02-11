from django.db import models

# Create your models here.
from django.test import TestCase

# Create your tests here.
from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

class People(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    class Role(models.TextChoices):
        REGULAR = 'R'
        ADMIN = 'A'

    role = models.CharField(
        max_length=1,
        choices=Role.choices,
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

