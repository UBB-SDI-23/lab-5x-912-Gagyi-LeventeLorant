from django.forms import ModelForm
from rest_framework import serializers
from .models import Film, Location, FilmOnLocation
from .models import Screening, Actor, ActedInFilm


class FilmSerializer(serializers.ModelSerializer):
    nr_of_screenings = serializers.IntegerField(read_only=True)
    average_pay = serializers.FloatField(read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'name', 'release_date', 'on_netfilx', 'profit', 'description', 'rating', 'nr_of_screenings', 'average_pay']


class FilmForm(ModelForm):
    class Meta:
        model = Film

        fields = ['name', 'release_date', 'on_netfilx', 'profit', 'rating', 'description']

    def clean(self):

        data = super(FilmForm, self).clean()

        print(data)

        name = data.get('name')
        rating = data.get('rating')

        print(name)
        print(rating)

        if rating < 0:
            self._errors['text'] = self.error_class([
                'Rating can\'t be negative'])
        if len(name) < 2:
            self._errors['name'] = self.error_class([
                'Minimum 2 characters required'])


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class FilmScreeningSerializer(serializers.ModelSerializer):
    screenings = ScreeningSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Film
        fields = ['name', 'release_date', 'on_netfilx', 'profit', 'rating', 'description', 'screenings']


class ScreeningWithFilm(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = ['room', 'date', 'imax', 'tickets_bought', 'price', 'film']
        depth = 1


class ActorsInFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActedInFilm
        fields = '__all__'


class ActorsInFilmSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = ActedInFilm
        fields = '__all__'
        depth = 1


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class FilmedOnLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmOnLocation
        fields = '__all__'


class FilmedOnLocationSerializerDetailed(serializers.ModelSerializer):
    class Meta:
        model = FilmOnLocation
        fields = '__all__'
        depth = 1


class FilmsByActorPaymentSerializer(serializers.ModelSerializer):
    average_pay = serializers.SerializerMethodField()

    def get_average_pay(self, obj):
        if obj.average_pay == None:
            return 0.0
        return obj.average_pay

    class Meta:
        model = Film
        fields = ['name', 'release_date', 'on_netfilx', 'profit', 'rating', 'average_pay']
