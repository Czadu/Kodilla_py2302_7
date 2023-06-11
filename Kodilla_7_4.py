
import random
import datetime

date = datetime.datetime.now()

movie_collection = [    {'Title': 'Kiler', 'Year': '1999', 'Genre': 'Comedy'},    
                        {'Title': 'Detektyw Bruno', 'Year': '2022', 'Genre': 'Family movie'},    
                        {'Title': 'Filip', 'Year': '2023', 'Genre': 'Drama'},    
                        {'Title': 'Proceder', 'Year': '2019', 'Genre': 'Biography'}
                    ]

series_collection = [ 
                        {'Title' : "Fury", 'Year' : '2021', 'Genre' : 'Thriller'},
                        {'Title' : "LOL", 'Year' : '2023', 'Genre' : 'Reality'},
                        {'Title' : "LNL", 'Year' : '2023', 'Genre' : 'Reality'}
                      ]

class Movie:
   def __init__(self, title, year, genre, views):
      self.title = title
      self.year = year
      self.genre = genre
      self.views = views
   def __str__(self):
      return f"\nTitle: {self.title} \nYear: {self.year} \nGenre: {self.genre}\nViews: {self.views}\n"
   def play(self, step=1):
      self.views += step

class Series(Movie):
   def __init__(self, episode, season, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.episode = episode
      self.season = season
   def __str__(self):
      return f"\nTitle: {self.title} \nYear: {self.year} \nGenre: {self.genre}\nS0{self.season} E0{self.episode} \nViews: {self.views}\n"



def search(movies, title):
    for i in movies:
        if title in i.title:
            return i
    return None

      
def get_movies(collection):
    only_movies = []
    for item in collection:
        if type(item) == Movie:
            only_movies.append(item)
    return only_movies


def get_series(collection):
    only_series = []
    for item in collection:
        if type(item) == Series:
            only_series.append(item)
    return only_series



def generate_views(movies):
    selected_movie = random.choice(movies)
    views_increment = random.randint(1, 100)
    selected_movie.play(views_increment)
    return 

def generate_views_10(movies):
   for i in range (10):
      generate_views(movies)

def top_titles(n):
    sorted_movies = sorted(movies, key=lambda x: x.views, reverse=True)
    top_n = sorted_movies[:n]
    return top_n



if __name__ == "__main__":


   movies = []

   for movie_dict in movie_collection:
      movie_obj = Movie(title=movie_dict['Title'], year=movie_dict['Year'], genre=movie_dict['Genre'], views=0)
      movies.append(movie_obj)
   for series_dict in series_collection:
      series_obj = Series(title=series_dict['Title'], year=series_dict['Year'], genre=series_dict['Genre'], views=0, season = f'{random.randrange(4)}', episode = f'{random.randrange(7)}')
      movies.append(series_obj)
   
   only_movies = get_movies(movies)
   only_movies.sort(key=lambda x: x.title)
   only_series = get_series(movies)
   only_series.sort(key=lambda x: x.title)
   by_views = sorted(movies, key = lambda y: y.views)

   random_movie = generate_views(movies)
   top_movies = top_titles(3)
   for content in movies:
      content.play(random.randrange(100))


   print('Film Collection:')
   for content in by_views:
      print (content.__str__())
   print()
   print(f'Most popular titles of a day {date.strftime("%d" " " "%b" " " "%y")}\n')
   for movie in top_movies:
      print(f'Title: {movie.title}\nViews: {movie.views}\n')   
   print(search(movies, "Kiler"))

