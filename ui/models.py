from django.db import models


class Site(models.Model):
    date = models.DateField()
    a = models.FloatField()
    b = models.FloatField()

    def __str__(self):
        return '<date: {}, a: {}, b: {}'.format(self.date, self.a, self.b)
