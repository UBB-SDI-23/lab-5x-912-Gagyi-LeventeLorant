from django.test import TestCase, Client
from django.urls import reverse
from films.models import Film, Screening, Actor, ActedInFilm
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        film1 = Film.objects.create(
            name="first",
            release_date = "2002-02-02",
            on_netfilx = False,
            profit = 100000,
            rating = 9.9,
        )
        film2 = Film.objects.create(
            name="second",
            release_date="2002-02-02",
            on_netfilx=False,
            profit=100000,
            rating=9.9,
        )
        film3 = Film.objects.create(
            name="third",
            release_date="2002-02-02",
            on_netfilx=False,
            profit=100000,
            rating=9.9,
        )

        Screening.objects.create(
            room="first",
            date = "2002-02-02",
            imax = False,
            tickets_bought = 100000,
            price = 9.9,
            film = film3,
        )
        Screening.objects.create(
            room="second",
            date = "2002-02-02",
            imax = False,
            tickets_bought = 100000,
            price = 9.9,
            film = film2,
        )
        Screening.objects.create(
            room="third",
            date = "2002-02-02",
            imax = False,
            tickets_bought = 100000,
            price = 9.9,
            film = film2,
        )


        act1 = Actor.objects.create(
            name="Act1",
            birth_date = "2002-02-02",
            married = False,
            films = 3,
            height = 123.4,
        )

        ActedInFilm.objects.create(
            film = film3,
            actor = act1,
            role = "idono",
            payment = 6000,
        )

        ActedInFilm.objects.create(
            film=film1,
            actor=act1,
            role="idono",
            payment=2000,
        )

        ActedInFilm.objects.create(
            film=film1,
            actor=act1,
            role="idono",
            payment=3000,
        )

    def test_Film_GET(self):

        response = self.client.get(reverse("film"))

        self.assertEquals(response.status_code, 200)

    def test_Film_detailed_GET(self):

        response = self.client.get(reverse("film_details", args=[1]))

        self.assertEquals(response.status_code, 200)

        response = self.client.get(reverse("film_details", args=[4]))

        self.assertEquals(response.status_code, 404)

    def test_Films_by_Screenings_GET(self):

        response = self.client.get(reverse("films_by_screenings"))

        self.assertEquals(response.status_code, 200)


        self.assertEquals(response.data[0]['name'], "second")
        self.assertEquals(response.data[0]['nr_of_screenings'], 2)
        self.assertEquals(response.data[1]['name'], "third")
        self.assertEquals(response.data[1]['nr_of_screenings'], 1)
        self.assertEquals(response.data[2]['nr_of_screenings'], 0)


    def test_film_by_actor_payment_list_GET(self):


        response = self.client.get(reverse("film_by_actor_payment_list"))

        self.assertEquals(response.status_code, 200)

        self.assertEquals(response.data[0]["average_pay"], 6000)
        self.assertEquals(response.data[1]["average_pay"], 2500)