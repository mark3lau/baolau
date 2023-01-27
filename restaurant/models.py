from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# STATUS = ((0, "Draft"), (1, "Published"))


class Reservation(models.Model):
    date = models.DateTimeField(null=False)
    time = models.DateTimeField(null=False)
    number_of_people = models.FloatField(max(0, 10), null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.date

