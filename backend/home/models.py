from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    used = models.BigIntegerField()


class Himanshutest(models.Model):
    "Generated Model"
    user = models.BigIntegerField()
