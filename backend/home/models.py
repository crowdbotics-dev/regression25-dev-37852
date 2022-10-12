from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    used = models.BigIntegerField()


class Himanshutest(models.Model):
    "Generated Model"
    user = models.BigIntegerField()
    test = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Usertest(models.Model):
    "Generated Model"
    addedtestadata = models.BigIntegerField()


class Addeddata(models.Model):
    "Generated Model"
    himanshu = models.BigIntegerField()
