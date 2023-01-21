from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.TextField(null=False, blank=False)
    contact_number = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    number_of_people = models.FloatField(max(0, 10), null=False, blank=False)

    def __str__(self):
        return self.date

