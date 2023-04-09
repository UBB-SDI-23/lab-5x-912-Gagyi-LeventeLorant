import random

from faker import Faker

fake = Faker()

n = 1000

with open('film_insert.sql', 'w') as f:
    for i in range(n):

        name = fake.sentence(nb_words=4)
        release_date = fake.date()
        on_netfilx = fake.pybool()
        profit = fake.random_int(1000000, 10000000)
        rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10

        film_sql = "INSERT INTO films_film(name, release_date, on_netfilx, profit, rating)" \
                   " VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit, rating)

        for j in range(n):
            name = fake.sentence(nb_words=4)
            release_date = fake.date()
            on_netfilx = fake.pybool()
            profit = fake.random_int(1000000, 10000000)
            rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10
            film_sql = film_sql + ", ('{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit,
                                                                            rating)

        film_sql = film_sql + ";\n"
        f.write(film_sql)

print("film_insert done")

with open('screening_insert.sql', 'w') as f:
    for i in range(n):

        room = fake.sentence(nb_words=1)[0] + str(fake.random_digit())
        date = fake.date()
        imax = fake.pybool()
        tickets_bought = fake.random_int(1, 100)
        price = fake.random_int(5, 25) + fake.random_int(0, 100) / 100
        film_id = random.randint(1, 999999)

        screening_sql = "INSERT INTO films_screening(room, date, imax, tickets_bought, price, film_id)" \
                        " VALUES ('{}', '{}', '{}', '{}', '{}', '{}')" \
            .format(room, date, imax, tickets_bought, price, film_id)

        for j in range(n):
            room = fake.sentence(nb_words=1)[0] + str(fake.random_digit())
            date = fake.date()
            imax = fake.pybool()
            tickets_bought = fake.random_int(1, 100)
            price = fake.random_int(5, 25) + fake.random_int(0, 100) / 100
            film_id = random.randint(1, 999999)

            screening_sql = screening_sql + ", ('{}', '{}', '{}', '{}', '{}', '{}')" \
                .format(room, date, imax, tickets_bought, price, film_id)

        screening_sql = screening_sql + ";\n"
        f.write(screening_sql)

print("screening_insert done")

with open('actor_insert.sql', 'w') as f:
    for i in range(n):

        name = fake.name()
        birth_date = fake.date()
        married = fake.pybool()
        films = fake.random_int(1, 100)
        height = 1 + fake.random_int(50, 99) / 100

        actor_sql = "INSERT INTO films_screening(name, birth_date, married, films, height)" \
                    " VALUES ('{}', '{}', '{}', '{}')" \
            .format(name, birth_date, married, films)

        for j in range(n):
            name = fake.name()
            birth_date = fake.date()
            married = fake.pybool()
            films = fake.random_int(1, 100)
            height = 1 + fake.random_int(50, 99) / 100

            actor_sql = actor_sql + ", ('{}', '{}', '{}', '{}')" \
                .format(name, birth_date, married, films)

        actor_sql = actor_sql + ";\n"
        f.write(actor_sql)

print("actor_insert done")

with open('acted_in_film_insert.sql', 'w') as f:
    for i in range(n * 10):

        role = fake.sentence(nb_words=1)
        payment = fake.random_int(10000, 1000000)
        film_id = random.randint(1, 999999)
        actor_id = random.randint(1, 999999)

        acted_in_film_sql = "INSERT INTO films_screening(film_id, actor_id, role, payment)" \
                            " VALUES ('{}', " \
                            "'{}', '{}', '{}')" \
            .format(film_id, actor_id, role, payment)

        for j in range(n):
            role = fake.sentence(nb_words=1)
            payment = fake.random_int(10000, 1000000)
            film_id = random.randint(1, 999999)
            actor_id = random.randint(1, 999999)

            acted_in_film_sql = acted_in_film_sql + ", ('{}', '{}', '{}', '{}')"\
                                                    .format(film_id, actor_id, role, payment)

        acted_in_film_sql = acted_in_film_sql + ";\n"
        f.write(acted_in_film_sql)

print("acted_in_film_insert done")

with open('location_insert.sql', 'w') as f:
    for i in range(n):

        name = fake.sentence(nb_words=2)
        country = fake.country()
        is_outdoors = fake.pybool()

        location_sql = "INSERT INTO films_screening(film_id, actor_id, role, payment)" \
                       " VALUES ('{}', '{}', '{}')" \
            .format(name, country, is_outdoors)

        for j in range(n):
            name = fake.sentence(nb_words=2)
            country = fake.country()
            is_outdoors = fake.pybool()

            location_sql = location_sql + ", ('{}', '{}', '{}')".format(name, country, is_outdoors)

        location_sql = location_sql + ";\n"
        f.write(location_sql)

print("location_insert done")

with open('film_on_location_insert.sql', 'w') as f:
    for i in range(n):

        nr_of_scenes = fake.random_int(1, 50)
        is_main = fake.pybool()
        film_id = random.randint(1, 999999)
        location_id = random.randint(1, 999999)

        film_on_location_sql = "INSERT INTO films_screening(film_id, location_id, nr_of_scenes, is_main) VALUES " \
                               "('{}', '{}', '{}', '{}')" \
            .format(film_id, location_id, nr_of_scenes, is_main)

        for j in range(n):
            nr_of_scenes = fake.random_int(1, 50)
            is_main = fake.pybool()
            film_id = random.randint(1, 999999)
            location_id = random.randint(1, 999999)

            film_on_location_sql = film_on_location_sql + ", ('{}', '{}', '{}', '{}')"\
                                                        .format(film_id, location_id, nr_of_scenes, is_main)

        film_on_location_sql = film_on_location_sql + ";\n"
        f.write(film_on_location_sql)

print("film_on_location_insert done")
