from classes.movie import Movie
from classes.viewer import Viewer


class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        type(self).all.append(self)

    # Review - rating getter/setter
    @property
    def rating(self):
        return self._rating

    # Ratings must be ints between 1-5, inclusive:
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception

    # Review - viewer getter/setter
    @property
    def viewer(self):
        return self._viewer

    # Viewers must be Viewer instances. Raise exception:
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception

    # Review - movie getter/setter
    @property
    def movie(self):
        return self._movie

    # Movie must be movie instances. Raise exception:
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception
