from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import actor_views
from . import film_views
from . import location_views
from . import screening_views

urlpatterns = [
    path('films/', film_views.FilmList.as_view(), name='film'),
    path('films/<int:id>', film_views.FilmDetails.as_view(), name='film_details'),
    path('films/filter/<int:filter_nr>', film_views.FilmFilter.as_view(), name='film_filter'),

    path('screenings/', screening_views.ScreeningList.as_view(), name='screenings'),
    path('screenings/<int:id>', screening_views.ScreeningDetails.as_view(), name='screening_details'),

    path('actors/', actor_views.ActorList.as_view(), name='actors'),
    path('actors/<int:id>', actor_views.ActorDetails.as_view(), name='actor_details'),

    path('acted_in/', actor_views.ActedInFilmList.as_view(), name='acted_in'),
    path('acted_in/<int:id>', actor_views.ActedInFilmDetail.as_view(), name='acted_in_details'),

    path('locations/', location_views.LocationList.as_view(), name='locations'),
    path('locations/<int:id>', location_views.LocationDetails.as_view(), name='locations_details'),

    path('film_on_location/', film_views.FilmOnLocationList.as_view(), name='film_on_location'),
    path('film_on_location/<int:id>', film_views.FilmOnLocationDetail.as_view(), name='film_on_location_details'),

    path('films_pay/', film_views.FilmsByActorPayment.as_view(), name='film_by_actor_payment_list'),

    path('films_by_screenings/', film_views.FilmsByScreenings.as_view(), name='films_by_screenings'),

    path('<int:id>/add_screenings/', screening_views.MultipleScreeningsToFilm.as_view(), name='multiple_screenings_to_film')


]

urlpatterns = format_suffix_patterns(urlpatterns)