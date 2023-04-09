from faker import Faker

fake = Faker()

# generate fake data
name = fake.name()
release_date = fake.date()
on_netfilx = fake.pybool()
profit = fake.random_int(1000000, 10000000)
rating = fake.random_int(1, 9) + fake.random_int(0, 10) / 10

# create INSERT SQL statement
sql = "INSERT INTO Film(name, release_date, on_netfilx, profit, rating) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, release_date, on_netfilx, profit, rating)

# write SQL statement to file
with open('film_insert.sql', 'w') as f:
    f.write(sql)
