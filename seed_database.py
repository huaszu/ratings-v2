"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())


movies_in_db = []
for movie in movie_data:
    title = movie["title"]
    overview = movie["overview"]
    poster_url = movie["poster_path"]
    date_str = movie["release_date"]
    format = "%Y-%m-%d"
    release_date = datetime.strptime(date_str, format)
    
    movie_in_db = crud.create_movie(title=title,
                                    overview=overview, 
                                    poster_path=poster_url, 
                                    release_date=release_date)
    movies_in_db.append(movie_in_db)

model.db.session.add_all(movies_in_db)
model.db.session.commit()


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email=email, password=password)
    model.db.session.add(user)
    model.db.session.commit()

    for num in range(10):
        movie_choice = choice(movies_in_db)
        rating_score = randint(1, 5)

        rating = crud.create_rating(user = user, 
                           movie = movie_choice, 
                           score = rating_score)
        model.db.session.add(rating)
        model.db.session.commit()