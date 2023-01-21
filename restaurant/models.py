from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    number = models.FloatField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False, default=False)
    time = models.TimeField(null=False, blank=False, default=False)
    number_of_people = models.FloatField(max(0, 10), null=False, blank=False)

    def __str__(self):
        return self.date

