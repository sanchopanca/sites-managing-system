from django.db import models


class Site(models.Model):
    date = models.DateField()
    a = models.FloatField()
    b = models.FloatField()
