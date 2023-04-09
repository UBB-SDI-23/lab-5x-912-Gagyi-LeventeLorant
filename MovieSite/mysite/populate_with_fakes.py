import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_example.settings')

django.setup()


from films.models import Film, Screening


if __name__ == '__main__':
    from faker import Faker

    fake = Faker()

    n = 10000
    for _ in range(n):

        Film.objects.create(name=fake.name(), release_date=fake.date(), on_netfilx=fake.pybool(), profit=fake.random_int(1000000, 10000000), rating=fake.random_float(1,10))
        Screening.objects.create(room=fake.name(), date=fake.date(),imax=fake.pybool(), tickets_bought=fake.random_int(1, 100), price= fake.random_float(5,25), film=Film.objects.last())