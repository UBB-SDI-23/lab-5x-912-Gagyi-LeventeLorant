import random

from faker import Faker

fake = Faker()

n = 1000
'''
with open('film_insert.sql', 'w') as f:
    f.write('TRUNCATE TABLE films_film RESTART IDENTITY CASCADE;\n')
    for i in range(n):

        name = fake.sentence(nb_words=4)
        release_date = fake.date()
        on_netfilx = fake.pybool()
        profit = fake.random_int(1000000, 10000000)
        rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10
        description = ""

        for k in range(10):
            description = description + fake.sentence(nb_words=10, variable_nb_words=False) + " "


        film_sql = "INSERT INTO films_film(name, release_date, on_netfilx, profit, rating, description)" \
                   " VALUES ('{}', '{}', '{}', '{}', '{}','{}')".format(name, release_date, on_netfilx, profit, rating,
                                                                        description)

        for j in range(n):
            name = fake.sentence(nb_words=4)
            release_date = fake.date()
            on_netfilx = fake.pybool()
            profit = fake.random_int(1000000, 10000000)
            rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10
            description = ""

            for l in range(10):
                description = description + fake.sentence(nb_words=10, variable_nb_words=False) + " "

            film_sql = film_sql + ", ('{}', '{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit,
                                                                            rating, description)

        film_sql = film_sql + ";\n"
        f.write(film_sql)

print("film_insert done")

with open('screening_insert.sql', 'w') as f:

    f.write('TRUNCATE TABLE films_screening RESTART IDENTITY CASCADE;\n')

    f.write('ALTER TABLE films_actor DROP CONSTRAINT films_screenings_film_id_c2e2d202_fk_films_film_id;\n')

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

    f.write('ALTER TABLE films_actor ADD CONSTRAINT films_screenings_film_id_c2e2d202_fk_films_film_id FOREIGN KEY (film_id) REFERENCES films_film(id) DEFERRABLE INITIALLY DEFERRED;\n')

print("screening_insert done")

with open('actor_insert.sql', 'w') as f:


    f.write('TRUNCATE TABLE films_actor RESTART IDENTITY CASCADE;\n')

    for i in range(n):

        name = fake.name()
        birth_date = fake.date()
        married = fake.pybool()
        films = fake.random_int(1, 100)
        height = 1 + fake.random_int(50, 99) / 100

        actor_sql = "INSERT INTO films_actor(name, birth_date, married, films, height)" \
                    " VALUES ('{}', '{}', '{}', '{}', '{}')" \
            .format(name, birth_date, married, films, height)

        for j in range(n):
            name = fake.name()
            birth_date = fake.date()
            married = fake.pybool()
            films = fake.random_int(1, 100)
            height = 1 + fake.random_int(50, 99) / 100

            actor_sql = actor_sql + ", ('{}', '{}', '{}', '{}', '{}')" \
                .format(name, birth_date, married, films, height)

        actor_sql = actor_sql + ";\n"
        f.write(actor_sql)

print("actor_insert done")
'''
pairs = set()

with open('acted_in_film_insert.sql', 'w') as f:


    f.write('TRUNCATE TABLE films_actedinfilm RESTART IDENTITY CASCADE;\n')

    f.write('ALTER TABLE films_actedinfilm DROP CONSTRAINT films_actedinfilm_actor_id_4c0cb276_fk_films_actor_id;\n')
    f.write('ALTER TABLE films_actedinfilm DROP CONSTRAINT films_actedinfilm_film_id_6263cfb1_fk_films_film_id;\n')

    for i in range(n * 10):

        role = fake.sentence(nb_words=1)
        payment = fake.random_int(10000, 1000000)
        film_id = random.randint(1, 999999)
        actor_id = random.randint(1, 999999)

        while (film_id, actor_id) in pairs:
            film_id = random.randint(1, 999999)
            actor_id = random.randint(1, 999999)

        acted_in_film_sql = "INSERT INTO films_actedinfilm(film_id, actor_id, role, payment)" \
                            " VALUES ('{}', " \
                            "'{}', '{}', '{}')" \
            .format(film_id, actor_id, role, payment)

        pairs.add((film_id, actor_id))

        for j in range(n):
            role = fake.sentence(nb_words=1)
            payment = fake.random_int(10000, 1000000)
            film_id = random.randint(1, 999999)
            actor_id = random.randint(1, 999999)

            while (film_id, actor_id) in pairs:
                film_id = random.randint(1, 999999)
                actor_id = random.randint(1, 999999)

            acted_in_film_sql = acted_in_film_sql + ", ('{}', '{}', '{}', '{}')"\
                                                    .format(film_id, actor_id, role, payment)

            pairs.add((film_id, actor_id))


        acted_in_film_sql = acted_in_film_sql + ";\n"
        f.write(acted_in_film_sql)

    f.write('ALTER TABLE films_actedinfilm ADD CONSTRAINT films_actedinfilm_actor_id_4c0cb276_fk_films_actor_id FOREIGN KEY (actor_id) REFERENCES films_actor(id) DEFERRABLE INITIALLY DEFERRED;\n')
    f.write('ALTER TABLE films_actedinfilm ADD CONSTRAINT films_actedinfilm_film_id_6263cfb1_fk_films_film_id FOREIGN KEY (film_id) REFERENCES films_film(id) DEFERRABLE INITIALLY DEFERRED;\n')

print("acted_in_film_insert done")

with open('location_insert.sql', 'w') as f:

    f.write('TRUNCATE TABLE films_location RESTART IDENTITY CASCADE;\n')

    for i in range(n):

        name = fake.sentence(nb_words=2)
        country_raw = fake.country()
        country = country_raw.replace("'"," ")
        is_outdoors = fake.pybool()

        location_sql = "INSERT INTO films_location(name, country, is_outdoors)" \
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

pairs = set()

with open('film_on_location_insert.sql', 'w') as f:

    f.write('TRUNCATE TABLE films_filmonlocation RESTART IDENTITY CASCADE;\n')

    f.write('ALTER TABLE films_filmonlocation DROP CONSTRAINT films_filmonlocation_film_id_96e67c87_fk_films_film_id;\n')
    f.write('ALTER TABLE films_filmonlocation DROP CONSTRAINT films_filmonlocation_location_id_8dbdaf21_fk_films_location_id;\n')

    for i in range(n):

        nr_of_scenes = fake.random_int(1, 50)
        is_main = fake.pybool()
        film_id = random.randint(1, 999999)
        location_id = random.randint(1, 999999)

        while (film_id, location_id) in pairs:
            film_id = random.randint(1, 999999)
            location_id = random.randint(1, 999999)

        film_on_location_sql = "INSERT INTO films_filmonlocation(film_id, location_id, nr_of_scenes, is_main) VALUES " \
                               "('{}', '{}', '{}', '{}')" \
            .format(film_id, location_id, nr_of_scenes, is_main)

        pairs.add((film_id, location_id))

        for j in range(n):
            nr_of_scenes = fake.random_int(1, 50)
            is_main = fake.pybool()
            film_id = random.randint(1, 999999)
            location_id = random.randint(1, 999999)

            while (film_id, location_id) in pairs:
                film_id = random.randint(1, 999999)
                location_id = random.randint(1, 999999)

            film_on_location_sql = film_on_location_sql + ", ('{}', '{}', '{}', '{}')"\
                                                        .format(film_id, location_id, nr_of_scenes, is_main)

            pairs.add((film_id, location_id))

        film_on_location_sql = film_on_location_sql + ";\n"
        f.write(film_on_location_sql)

    f.write('ALTER TABLE films_filmonlocation ADD CONSTRAINT films_filmonlocation_film_id_96e67c87_fk_films_film_id FOREIGN KEY (film_id) REFERENCES films_film(id) DEFERRABLE INITIALLY DEFERRED;\n')
    f.write('ALTER TABLE films_filmonlocation ADD CONSTRAINT films_filmonlocation_location_id_8dbdaf21_fk_films_location_id FOREIGN KEY (location_id) REFERENCES films_location(id) DEFERRABLE INITIALLY DEFERRED;\n')

print("film_on_location_insert done")
