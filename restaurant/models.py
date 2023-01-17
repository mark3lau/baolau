from django.db import models

# Create your models here.
class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField(max(0, 10), null=False, blank=False)
