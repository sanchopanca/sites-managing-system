from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return '<Site: {}>'.format(self.name)


class Statistics(models.Model):
    site = models.ForeignKey(Site, related_name='statistics_entries',
                             on_delete=models.CASCADE)
    date = models.DateField()
    a = models.FloatField()
    b = models.FloatField()

    def __str__(self):
        return '<{}, date: {}, a: {}, b: {}'.\
            format(self.site, self.date, self.a, self.b)
