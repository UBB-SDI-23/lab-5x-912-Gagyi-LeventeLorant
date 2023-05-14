from datetime import timezone, datetime

from django.db import models
from django.db.models import Avg
from django.forms import ModelForm
from rest_framework.pagination import PageNumberPagination


# Create your models here.


class Film(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateTimeField('Release date')
    on_netfilx = models.BooleanField(default=False)
    profit = models.IntegerField()
    rating = models.FloatField()
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

    @property
    def average_pay(self):
        if hasattr(self, '_average_pay'):
            return self._average_pay
        return self.film.aggregate(Avg('payment'))["payment__avg"]


class Screening(models.Model):
    room = models.CharField(max_length=200)
    date = models.DateTimeField('Screening date')
    imax = models.BooleanField(default=False)
    tickets_bought = models.IntegerField()
    price = models.FloatField()
    film = models.ForeignKey(Film, related_name='screenings', on_delete=models.CASCADE)

    def __str__(self):
        return self.room


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('Birth date')
    married = models.BooleanField(default=False)
    films = models.IntegerField()
    height = models.FloatField()

    def __str__(self):
        return self.name


class ActedInFilm(models.Model):
    film = models.ForeignKey(Film, related_name='film', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name='actors', on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    payment = models.IntegerField()

    def __str__(self):
        return str(self.actor) + " in " + str(self.film)


class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_outdoors = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FilmOnLocation(models.Model):
    film = models.ForeignKey(Film, related_name='locationfilm', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='locations', on_delete=models.CASCADE)
    nr_of_scenes = models.IntegerField()
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return str(self.film) + " shoot in " + str(self.location)



