'''CRUD operations.'''

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def get_users():
    '''Returns all users from database'''

    return User.query.all()    


def get_user_by_id(user_id):
    '''Returns user for user_id.'''

    return User.query.filter_by(user_id=user_id).all()[0]


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, 
                  overview=overview,
                  release_date=release_date,
                  poster_path=poster_path)

    return movie


def get_movies():
    '''Returns all movies from database'''

    return Movie.query.all()


def get_movie_by_id(movie_id):
    '''Returns movie for movie_id.'''

    # Movie.query.filter_by(movie_id=movie_id).all() is a list

    return Movie.query.filter_by(movie_id=movie_id).all()[0]


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
