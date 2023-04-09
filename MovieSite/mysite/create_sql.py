from faker import Faker

fake = Faker()

name = fake.name()
release_date = fake.date()
on_netfilx = fake.pybool()
profit = fake.random_int(1000000, 10000000)
rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10

# generate fake data

# create INSERT SQL statement
film_sql = "INSERT INTO films_film(name, release_date, on_netfilx, profit, rating)" \
           " VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit, rating)

n = 100

for i in range(n):
    name = fake.name()
    release_date = fake.date()
    on_netfilx = fake.pybool()
    profit = fake.random_int(1000000, 10000000)
    rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10
    film_sql = film_sql + ", ('{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit, rating)

# write SQL statement to file
with open('film_insert.sql', 'w') as f:
    f.write(film_sql)

room = fake.name()
date = fake.date()
imax = fake.pybool()
tickets_bought = fake.random_int(1, 100)
price = fake.random_int(5, 25) + fake.random_int(0, 100) / 100

screening_sql = "INSERT INTO films_screening(room, date, tickets_bought, price, film)" \
                " VALUES ('{}', '{}', '{}', '{}', 'SELECT id FROM films_film ORDER BY RANDOM() LIMIT 1')" \
    .format(room, date, tickets_bought, price)

for i in range(n):
    room = fake.name()
    date = fake.date()
    imax = fake.pybool()
    tickets_bought = fake.random_int(1, 100)
    price = fake.random_int(5, 25) + fake.random_int(0, 100) / 100
    screening_sql = screening_sql + ", ('{}', '{}', '{}', '{}', 'SELECT id FROM films_film ORDER BY RANDOM() LIMIT 1')" \
        .format(room, date, tickets_bought, price)

with open('screening_insert.sql', 'w') as f:
    f.write(screening_sql)