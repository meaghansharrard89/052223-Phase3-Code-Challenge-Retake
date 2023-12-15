class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    # Movie - title getter/setter:
    @property
    def title(self):
        return self._title

    # Titles must be strings greater than 0, raise Exception:
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception

    # Returns a list of all the Review instances for the Movie:
    def reviews(self):
        from classes.review import Review

        return [review for review in Review.all if review.movie == self]

    # Returns a list of all of the Viewer instances that reviewed the Movie:
    def reviewers(self):
        return [movie.viewer for movie in self.reviews()]

    # Returns the average of all ratings for the Movie instance:
    def average_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

    # Returns the Movie instance with the highest average rating:
    @classmethod
    def highest_rated(cls):
        if not cls.all:
            return None

        highest_rated = max(cls.all, key=lambda movie: movie.average_rating())
        return highest_rated
