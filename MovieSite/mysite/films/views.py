from django.db.models import Count, Avg
from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Film, Actor, ActedInFilm, Location, FilmOnLocation
from .serializers import FilmSerializer, ActorSerializer, ScreeningWithFilm, ActorsInFilmSerializer, \
    ActorsInFilmSerializerDetailed, LocationSerializer, FilmedOnLocationSerializer, FilmedOnLocationSerializerDetailed, \
    FilmsByActorPaymentSerializer, FilmForm
from .models import Screening
from .serializers import ScreeningSerializer, FilmScreeningSerializer


# @api_view(['GET', 'POST'])
# def film_list(request):
#
#     if request.method == 'GET':
#
#
#         films = Film.objects.all()
#         profit = request.query_params.get('profit')
#
#         if profit is not None:
#             films = films.filter(profit__gte=profit)
#
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     elif request.method == 'POST':
#
#         serializer = FilmForm(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)

class FilmList(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request, *args, **kwargs):
        # some actions
        films = Film.objects.all()
        profit = request.query_params.get('profit')

        if profit is not None:
            films = films.filter(profit__gte=profit)

        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @extend_schema(request=FilmSerializer, responses=FilmForm)
    def post(self, request):

        serializer = FilmForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)




class FilmDetails(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request, id):
        try:
            film = Film.objects.get(pk=id)
        except Film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FilmScreeningSerializer(film)
        return Response(serializer.data, status=status.HTTP_200_OK)



    @extend_schema(request=FilmSerializer, responses=FilmSerializer)
    def put(self, request, id):
        try:
            film = Film.objects.get(pk=id)
        except Film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(request=None, responses=None)
    def delete(self, request, id):

        try:
            film = Film.objects.get(pk=id)
        except Film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def film_details(request, id):
#
#     try:
#         film = Film.objects.get(pk=id)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = FilmScreeningSerializer(film)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = FilmSerializer(film, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         film.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class ScreeningList(APIView):

    @extend_schema(request=None, responses=ScreeningSerializer)
    def get(self, request):
        screenings = Screening.objects.all()
        serializer = ScreeningSerializer(screenings, many=True)
        return Response(serializer.data)

    @extend_schema(request=ScreeningSerializer, responses=ScreeningSerializer)
    def post(self, request):
        serializer = ScreeningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_418_IM_A_TEAPOT)


# @api_view(['GET', 'POST'])
# def screening_list(request):
#
#     if request.method == 'GET':
#         screenings = Screening.objects.all()
#         serializer = ScreeningSerializer(screenings, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ScreeningSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else: return Response(serializer.data, status=status.HTTP_418_IM_A_TEAPOT)


class MultipleScreeningsToFilm(APIView):

    @extend_schema(request=None, responses=ScreeningSerializer)
    def post(self, request, id):
        try:
            film = Film.objects.get(pk=id)

            if request.method == 'POST':
                data = request.data
                newitems = []

                for item in data:
                    newScreening = Screening.objects.create(
                        room=item.get('room'),
                        date=item.get('date'),
                        imax=item.get('imax'),
                        tickets_bought=item.get('tickets_bought'),
                        price=item.get('price'),
                        film=film,
                    )

                    newScreening.save()
                    newitems.append(newScreening)

                serializer = ScreeningSerializer(newitems, many=True)

                return Response(serializer.data)

        except Film.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def multiple_screenings_to_film(request, id):
#
#     try:
#         film = Film.objects.get(pk=id)
#
#         if request.method == 'POST':
#             data = request.data
#             newitems = []
#
#             for item in data:
#
#                 newScreening = Screening.objects.create(
#                     room=item.get('room'),
#                     date=item.get('date'),
#                     imax=item.get('imax'),
#                     tickets_bought=item.get('tickets_bought'),
#                     price=item.get('price'),
#                     film=film,
#                 )
#
#                 newScreening.save()
#                 newitems.append(newScreening)
#
#             serializer = ScreeningSerializer(newitems, many=True)
#
#             return Response(serializer.data)
#
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


class ScreeningDetails(APIView):
    @extend_schema(request=None, responses=ScreeningWithFilm)
    def get(self, request, id):
        try:
            screening = Screening.objects.get(pk=id)
        except Screening.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ScreeningWithFilm(screening)
        return Response(serializer.data)

    @extend_schema(request=ScreeningSerializer, responses=ScreeningSerializer)
    def put(self, request, id):
        try:
            screening = Screening.objects.get(pk=id)
        except Screening.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ScreeningSerializer(screening, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def delete(self, request, id):
        try:
            screening = Screening.objects.get(pk=id)
        except Screening.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        screening.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def screening_details(request, id):
#
#     try:
#         screening = Screening.objects.get(pk=id)
#     except Screening.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ScreeningWithFilm(screening)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ScreeningSerializer(screening, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         screening.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class FilmFilter(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request, filter_nr):
        films = Film.objects.filter(profit__gte=filter_nr)
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)



# @api_view(['GET'])
# def film_filter(request, filter_nr):
#
#     if request.method == 'GET':
#         films = Film.objects.filter(profit__gte=filter_nr)
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data)


class ActorList(APIView):
    @extend_schema(request=None, responses=ActorSerializer)
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)


    @extend_schema(request=ActorSerializer, responses=ActorSerializer)
    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def actor_list(request):
#
#     if request.method == 'GET':
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActorDetails(APIView):


    @extend_schema(request=None, responses=ActorSerializer)
    def get(self, request, id):

        try:
            actor = Actor.objects.get(pk=id)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    @extend_schema(request=ActorSerializer, responses=ActorSerializer)
    def put(self, request, id):

        try:
            actor = Actor.objects.get(pk=id)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def delete(self, request, id):

        try:
            actor = Actor.objects.get(pk=id)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'PUT', 'DELETE'])
# def actor_details(request, id):
#
#     try:
#         actor = Actor.objects.get(pk=id)
#     except Actor.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ActorSerializer(actor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ActedInFilmList(APIView):
    @extend_schema(request=None, responses=ActorsInFilmSerializer)
    def get(self, request):
        actors = ActedInFilm.objects.all()
        serializer = ActorsInFilmSerializer(actors, many=True)
        return Response(serializer.data)

    @extend_schema(request=ActorsInFilmSerializer, responses=ActorsInFilmSerializer)
    def post(self, request):
        serializer = ActorsInFilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['GET', 'POST'])
# def acted_in_film_list(request):
#
#     if request.method == 'GET':
#         actors = ActedInFilm.objects.all()
#         serializer = ActorsInFilmSerializer(actors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ActorsInFilmSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActedInFilmDetail(APIView):


    @extend_schema(request=None, responses=ActorsInFilmSerializer)
    def get(self, request, id):

        try:
            acted_in_film = ActedInFilm.objects.get(pk=id)
        except ActedInFilm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = ActorsInFilmSerializerDetailed(acted_in_film)
        return Response(serializer.data)

    @extend_schema(request=ActorsInFilmSerializer, responses=ActorsInFilmSerializer)
    def put(self, request, id):

        try:
            acted_in_film = ActedInFilm.objects.get(pk=id)
        except ActedInFilm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorsInFilmSerializer(acted_in_film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def delete(self, request, id):

        try:
            acted_in_film = ActedInFilm.objects.get(pk=id)
        except ActedInFilm.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        acted_in_film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'PUT', 'DELETE'])
# def acted_in_film_details(request, id):
#
#     try:
#         acted_in_film = ActedInFilm.objects.get(pk=id)
#     except ActedInFilm.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ActorsInFilmSerializerDetailed(acted_in_film)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ActorsInFilmSerializer(acted_in_film, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         acted_in_film.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class LocationList(APIView):
    @extend_schema(request=None, responses=LocationSerializer)
    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

    @extend_schema(request=LocationSerializer, responses=LocationSerializer)
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def location_list(request):
#
#     if request.method == 'GET':
#         location = Location.objects.all()
#         serializer = LocationSerializer(location, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

class LocationDetails(APIView):

    @extend_schema(request=None, responses=FilmedOnLocationSerializerDetailed)
    def get(self, request, id):

        try:
            location = Location.objects.get(pk=id)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LocationSerializer(location)
        return Response(serializer.data)

    @extend_schema(request=FilmedOnLocationSerializerDetailed, responses=FilmedOnLocationSerializerDetailed)
    def put(self, request, id):

        try:
            location = Location.objects.get(pk=id)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def delete(self, request, id):

        try:
            location = Location.objects.get(pk=id)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def location_details(request, id):
#
#     try:
#         location = Location.objects.get(pk=id)
#     except Location.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = LocationSerializer(location)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = LocationSerializer(location, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class FilmOnLocationList(APIView):
    @extend_schema(request=None, responses=FilmedOnLocationSerializer)
    def get(self, request):
        film_on_location = FilmOnLocation.objects.all()
        serializer = FilmedOnLocationSerializer(film_on_location, many=True)
        return Response(serializer.data)

    @extend_schema(request=FilmedOnLocationSerializer, responses=FilmedOnLocationSerializer)
    def post(self, request):
        serializer = FilmedOnLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def film_on_location_list(request):
#
#     if request.method == 'GET':
#         film_on_location = FilmOnLocation.objects.all()
#         serializer = FilmedOnLocationSerializer(film_on_location, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = FilmedOnLocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

class FilmOnLocationDetail(APIView):

    @extend_schema(request=None, responses=FilmedOnLocationSerializerDetailed)
    def get(self, request, id):

        try:
            film_on_location = FilmOnLocation.objects.get(pk=id)
        except FilmOnLocation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FilmedOnLocationSerializerDetailed(film_on_location)
        return Response(serializer.data)

    @extend_schema(request=FilmedOnLocationSerializerDetailed, responses=FilmedOnLocationSerializerDetailed)
    def put(self, request, id):

        try:
            film_on_location = FilmOnLocation.objects.get(pk=id)
        except FilmOnLocation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FilmedOnLocationSerializer(film_on_location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=None, responses=None)
    def delete(self, request, id):

        try:
            film_on_location = FilmOnLocation.objects.get(pk=id)
        except FilmOnLocation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        film_on_location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def film_on_location_details(request, id):
#
#     try:
#         film_on_location = FilmOnLocation.objects.get(pk=id)
#     except FilmOnLocation.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = FilmedOnLocationSerializerDetailed(film_on_location)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = FilmedOnLocationSerializer(film_on_location, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         film_on_location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class FilmsByScreenings(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request):

        films = Film.objects.annotate(nr_of_screenings=Count('screenings')).order_by('-nr_of_screenings')

        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def films_by_screenings(request):
#
#
#     if request.method == 'GET':
#
#         films = Film.objects.annotate(nr_of_screenings=Count('screenings')).order_by('-nr_of_screenings')
#
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class FilmsByActorPayment(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request):

        films = Film.objects.annotate(avg_pay=Avg('film__payment')).order_by('-avg_pay')

        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def film_by_actor_payment_list(request):
#
#
#     if request.method == 'GET':
#
#         films = Film.objects.annotate(avg_pay=Avg('film__payment')).order_by('-avg_pay')
#
#         serializer = FilmSerializer(films, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


