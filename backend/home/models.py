from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    used = models.BigIntegerField()


class Usertest(models.Model):
    "Generated Model"
    addedtestadata = models.BigIntegerField()
