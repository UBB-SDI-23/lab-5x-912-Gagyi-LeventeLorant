from django.core.paginator import Paginator
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Actor, ActedInFilm
from .paginators import CustomPagination
from .serializers import ActorSerializer, ActorsInFilmSerializer, ActorsInFilmSerializerDetailed


class ActorList(APIView, CustomPagination):

    @extend_schema(request=None, responses=ActorSerializer)
    def get(self, request):

        actors = Actor.objects.all()

        paginator = Paginator(actors, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = ActorSerializer(page_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @extend_schema(request=ActorSerializer, responses=ActorSerializer)
    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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


class ActedInFilmList(APIView):
    @extend_schema(request=None, responses=ActorsInFilmSerializer)
    def get(self, request, *args, **kwargs):
        actors = ActedInFilm.objects.all()

        paginator = Paginator(actors, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = ActorsInFilmSerializer(page_obj, many=True)
        return Response(serializer.data)

    @extend_schema(request=ActorsInFilmSerializer, responses=ActorsInFilmSerializer)
    def post(self, request):
        serializer = ActorsInFilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
