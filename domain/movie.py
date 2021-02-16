class Movie:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

    def get_movie_name(self):
        return self.__name

    def set_movie_name(self, name):
        self.__name = name
