from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.FilmList.as_view(), name='film'),
    path('<int:id>', views.FilmDetails.as_view(), name='film_details'),
    path('filter/<int:filter_nr>', views.FilmFilter.as_view(), name='film_filter'),

    path('screenings', views.ScreeningList.as_view(), name='screenings'),
    path('screenings/<int:id>', views.ScreeningDetails.as_view(), name='screening_details'),

    path('actors', views.ActorList.as_view(), name='actors'),
    path('actors/<int:id>', views.ActorDetails.as_view(), name='actor_details'),

    path('acted_in', views.ActedInFilmList.as_view(), name='acted_in'),
    path('acted_in/<int:id>', views.ActedInFilmDetail.as_view(), name='acted_in_details'),

    path('locations', views.LocationList.as_view(), name='locations'),
    path('locations/<int:id>', views.LocationDetails.as_view(), name='locations_details'),

    path('film_on_location', views.FilmOnLocationList.as_view(), name='film_on_location'),
    path('film_on_location/<int:id>', views.FilmOnLocationDetail.as_view(), name='film_on_location_details'),

    path('films_pay', views.FilmsByActorPayment.as_view(), name='film_by_actor_payment_list'),

    path('films_by_screenings', views.FilmsByScreenings.as_view(), name='films_by_screenings'),

    path('<int:id>/add_screenings', views.MultipleScreeningsToFilm.as_view(), name='multiple_screenings_to_film')


]

urlpatterns = format_suffix_patterns(urlpatterns)