class Movie:
    movies = {}

    def __init__(self, movie_name: str, director_name: str, producer_name: str, genre: str, language: str, duration: float, story: str):
        self.id = None  # To be assigned from the database or a generator
        self.movie_id = None  # This should be assigned separately
        self.movie_name = movie_name
        self.director_name = director_name
        self.producer_name = producer_name
        self.duration = duration
        self.story = story
        self.genre = genre
        self.language = language

    def display_movie_details(self):
        print(f"Movie ID : {self.movie_id}")
        print(f"Movie Name : {self.movie_name}")
        print(f"Producer Name : {self.producer_name}")
        print(f"Director Name : {self.director_name}")
        print(f"Language : {self.language}")
        print(f"Duration : {self.duration}")
        print(f"Genre : {self.genre}")
        print(f"Story : {self.story}")

    @classmethod
    def get_movies(cls):
        return cls.movies

    @classmethod
    def set_movies(cls, movies):
        cls.movies = movies

    def __repr__(self):
        return (f"Movie(MovieId={self.movie_id}, Name={self.movie_name}, "
                f"Director={self.director_name}, Producer={self.producer_name}, "
                f"Genre={self.genre}, Language={self.language}, Duration={self.duration})")

# Example usage:
if __name__ == "__main__":
    movie1 = Movie("Inception", "Christopher Nolan", "Emma Thomas", "Sci-Fi", "English", 2.5, "A mind-bending thriller")
    movie1.movie_id = "M123"
    movie1.display_movie_details()
