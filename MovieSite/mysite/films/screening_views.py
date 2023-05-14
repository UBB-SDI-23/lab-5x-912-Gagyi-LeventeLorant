from django.core.paginator import Paginator
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Screening, Film
from .serializers import ScreeningSerializer, ScreeningWithFilm


class ScreeningList(APIView):

    @extend_schema(request=None, responses=ScreeningSerializer)
    def get(self, request):
        screenings = Screening.objects.all()

        paginator = Paginator(screenings, 10)  # 10 objects per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        serializer = ScreeningSerializer(page_obj, many=True)
        return Response(serializer.data)

    @extend_schema(request=ScreeningSerializer, responses=ScreeningSerializer)
    def post(self, request):
        serializer = ScreeningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_418_IM_A_TEAPOT)


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
