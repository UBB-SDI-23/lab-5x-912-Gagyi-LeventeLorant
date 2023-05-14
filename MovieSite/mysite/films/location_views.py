from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Location
from .serializers import LocationSerializer, FilmedOnLocationSerializerDetailed


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
