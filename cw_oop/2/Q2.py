class Movie:
    def __init__(self, title, director, duration):
        self.set_title(title)
        self.set_director(director)
        self.set_duration(duration)

    def set_title(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        self.__title = title.strip()

    def get_title(self):
        return self.__title

    def set_director(self, director):
        if not isinstance(director, str) or not director.strip():
            raise ValueError("Director must be a non-empty string.")
        self.__director = director.strip()

    def get_director(self):
        return self.__director

    def set_duration(self, duration):
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def display_details(self):
        print(f"Title: {self.get_title()}")
        print(f"Director: {self.get_director()}")
        print(f"Duration: {self.get_duration()} minutes")

movie = Movie("filme aroosi", "film bardar", 72)
movie.display_details()