from django.contrib import admin

# Register your models here.
from .models import Film, Screening, Actor, ActedInFilm, Location, FilmOnLocation

# Register your models here.

admin.site.register(Film)

admin.site.register(Screening)

admin.site.register(Actor)

admin.site.register(ActedInFilm)

admin.site.register(Location)

admin.site.register(FilmOnLocation)
