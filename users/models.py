from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomerUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
