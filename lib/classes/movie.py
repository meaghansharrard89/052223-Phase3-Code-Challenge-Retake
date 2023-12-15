class Movie:
    all = []

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)

    # Movie-Title getter and setter
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review

        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return [review.viewer for review in self.reviews()]

    def average_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0

    @classmethod
    def highest_rated(cls):
        if not cls.all:
            return None

        highest_rated = max(cls.all, key=lambda movie: movie.average_rating())
        return highest_rated
