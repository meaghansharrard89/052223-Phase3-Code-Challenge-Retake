class Viewer:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    # Viewer - username getter/setter
    @property
    def username(self):
        return self._username

    # Usernames must be strings between 6-16 chars, inclusive. Raise exception. Usernames unique:
    @username.setter
    def username(self, username):
        if (
            not hasattr(self, "username")
            and isinstance(username, str)
            and 6 <= len(username) <= 16
        ):
            self._username = username
        else:
            raise Exception

    # Returns a list of Review instances associated with the Viewer instance:
    def reviews(self):
        from classes.review import Review

        return [review for review in Review.all if review.viewer == self]

    # Returns a list of Movie instances reviewed by the Viewer instance:
    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    # Returns True if the Viewer has reviewed this Movie (if there is a Review instance that has this Viewer and Movie), returns False otherwise:
    def has_reviewed_movie(self, movie):
        return any(review.movie == movie for review in self.reviews())
