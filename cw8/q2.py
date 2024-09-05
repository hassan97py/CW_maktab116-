import pickle

class FavoriteMovies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def remove_movie(self, movie):
        if movie in self.movies:
            self.movies.remove(movie)

    def list_movies(self):
        return self.movies

    def save_movies(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.movies, file)

    def load_movies(self, file_path):
        with open(file_path, 'rb') as file:
            self.movies = pickle.load(file)

# Create an instance of FavoriteMovies
movies = FavoriteMovies()

# Add some movies
movies.add_movie("The Shawshank Redemption")
movies.add_movie("The Godfather")
movies.add_movie("The Dark Knight")

# List all movies
print("Favorite Movies:", movies.list_movies())

# Save the movies to a file
movies.save_movies("movies.pkl")

# Create a new instance and load the movies
new_movies = FavoriteMovies()
new_movies.load_movies("movies.pkl")

# Check if the movies were loaded correctly
print("Loaded Movies:", new_movies.list_movies())