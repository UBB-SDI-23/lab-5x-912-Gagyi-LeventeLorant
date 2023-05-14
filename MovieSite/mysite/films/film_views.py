from django.core.paginator import Paginator
from django.db.models import Count, Avg
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Film, FilmOnLocation
from .serializers import FilmSerializer, FilmForm, FilmScreeningSerializer, FilmedOnLocationSerializer, \
    FilmedOnLocationSerializerDetailed


class FilmList(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request, *args, **kwargs):
        # some actions
        films = Film.objects.all()

        paginator = Paginator(films, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        profit = request.query_params.get('profit')

        if profit is not None:
            page_obj = films.filter(profit__gte=profit)

        serializer = FilmSerializer(page_obj, many=True)
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


class FilmOnLocationList(APIView):
    @extend_schema(request=None, responses=FilmedOnLocationSerializer)
    def get(self, request):
        film_on_location = FilmOnLocation.objects.all()

        paginator = Paginator(film_on_location, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = FilmSerializer(page_obj, many=True)
        return Response(serializer.data)

    @extend_schema(request=FilmedOnLocationSerializer, responses=FilmedOnLocationSerializer)
    def post(self, request):
        serializer = FilmedOnLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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


class FilmsByScreenings(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request):

        films = Film.objects.annotate(nr_of_screenings=Count('screenings')).order_by('-nr_of_screenings')

        paginator = Paginator(films, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = FilmSerializer(page_obj, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FilmsByActorPayment(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request):

        films = Film.objects.annotate(avg_pay=Avg('film__payment')).exclude(avg_pay__isnull=True).order_by('-avg_pay')

        # films = Film.objects.all().extra(
        #     {'avg_pay': 'SELECT AVG(films_actedinfilm.payment) FROM films_actedinfilm WHERE '
        #                 'films_actedinfilm.film_id = films_film.id'}).exclude(avg_pay='null').order_by('-avg_pay')

        paginator = Paginator(films, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = FilmSerializer(page_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FilmFilter(APIView):
    @extend_schema(request=None, responses=FilmSerializer)
    def get(self, request, filter_nr):
        films = Film.objects.filter(profit__gte=filter_nr)

        paginator = Paginator(films, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = FilmSerializer(page_obj, many=True)
        return Response(serializer.data)
