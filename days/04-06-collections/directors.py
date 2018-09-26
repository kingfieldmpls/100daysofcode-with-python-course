import csv
import time

from collections import defaultdict, namedtuple, Counter
from statistics import mean

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=MOVIE_DATA):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as md:
        reader = csv.DictReader(md)
        for line in reader:
            director = line["director_name"]
            title = line["movie_title"]
            year = line["title_year"]
            score = line["imdb_score"]

            m = Movie(title=title, year=year, score=score)
            directors[director].append(m)
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate average score'''
    # List Comprehension
    # for director in directors:
    #     if len(directors[director]) >= MIN_MOVIES:
    #         director_mean = [float(movie.score) for movie in directors[director]]
    #         print(director, round(mean(director_mean), 1))

    # Counter w/ helper function
    cnt = Counter()
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            cnt[director] += _calc_mean(movies)
    return cnt.most_common(20)


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(mean(float(movie.score) for movie in movies), 1)

# THIS IS WHERE I'M AT
def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    # print_results(directors)


if __name__ == '__main__':
    main()
