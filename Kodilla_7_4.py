
from __future__ import print_function
import random
import datetime

date = datetime.datetime.now()

print('Film Collection:')



class movie:
   def __init__(self, title, year, genre, views):
      self.title = title
      self.year = year
      self.genre = genre
      self.views = views
   def __str__(self):
      return f"\nTitle: {self.title} \nYear: {self.year} \nGenre: {self.genre}\nViews: {self.views}\n"
   def play(self, step=1):
      self.views += step
   

class series:
   def __init__(self, title, year, genre, episode, season, views):
      self.title = title
      self.year = year
      self.genre = genre
      self.episode = episode
      self.season = season
      self.views = views
   def __str__(self):
      return f"\nTitle: {self.title} \nYear: {self.year} \nGenre: {self.genre}\nS0{self.season} E0{self.episode} \nViews: {self.views}\n"
   def play(self, step=1):
      self.views += step
   

series1 = []

  

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


def search(movies):
   x = input('Name the title you are looking for: ')
   for i in movies:
      if x in i.title:
         print ("Selected movie is in our collection")
         return
      print ("There is no such thing")
      return
      
      


movies = []

for movie_dict in movie_collection:
    movie_obj = movie(title=movie_dict['Title'], year=movie_dict['Year'], genre=movie_dict['Genre'], views=0)
    movies.append(movie_obj)

for series_dict in series_collection:
    series_obj = series(title=series_dict['Title'], year=series_dict['Year'], genre=series_dict['Genre'], views=0, season = f'{random.randrange(4)}', episode = f'{random.randrange(7)}')
    movies.append(series_obj)


by_views = sorted(movies, key = lambda y: y.views)

def get_movies(movie):
   only_movies = []
   for item in movies:
      if isinstance(item, movie):
         only_movies.append(item)
   return only_movies


def get_series(series):
   only_series = []
   for item in movies:
      if isinstance(item, series):
         only_series.append(item)
   return only_series

only_movies = get_series(series)
only_movies.sort(key=lambda x: x.title)

only_series = get_movies(movie)
only_series.sort(key=lambda x: x.title)

def generate_views(movies):
    selected_movie = random.choice(movies)
    views_increment = random.randint(1, 100)
    selected_movie.play(views_increment)
    return selected_movie.__str__()

def generate_views_10(movies):
   for i in range (10):
      generate_views(movies)

random_movie = generate_views(movies)

for content in movies:
   content.play(random.randrange(100))



def top_titles(n):
    sorted_movies = sorted(movies, key=lambda x: x.views, reverse=True)
    top_n = sorted_movies[:n]
    return top_n
      
top_movies = top_titles(3)



### Biblioteka filmów na początek

for content in by_views:
  print (content.__str__())

print()
print(f'Most popular titles of a day {date.strftime("%d" " " "%b" " " "%y")}\n')
for movie in top_movies:
    print(f'Title: {movie.title}\nViews: {movie.views}\n')

###

print(search(movies))




