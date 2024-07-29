movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# q1) total_number_of_movies

movies_count = len(movies)
# print(movies_count)

# q2) movies with genre Drama

malayalam_movies = [mov.get("title") for mov in movies if "Drama" in mov.get("genres")]
# print(malayalam_movies)
        
# q3) latest movie

def get_year(mov):
    return mov.get("year")

latest_year_movie = max(movies, key=get_year)
latest_movies = [mov.get("title") for mov in movies if mov.get("year") == latest_year_movie.get("year")]
# print(latest_movies)

# q4) top movie (movie with highest rating)

def get_rating(mov):
    return mov.get("rating")

high_rated_movie = max(movies, key=get_rating)
top_movies = [mov.get("title") for mov in movies if mov.get("rating") == high_rated_movie.get("rating")]
# print(top_movies)

# q5) movies with language malayalam

malayalam_movies = [mov.get("title") for mov in movies if "Malayalam" == mov.get("language")]
# print(malayalam_movies)

# q6) movies released after year 2016

movies_after_2016 = [mov.get("title") for mov in movies if mov.get("year") > 2016]
# print(movies_after_2016)

# q7) movie with lowest rating

low_rated_movie = min(movies, key=get_rating)
low_movies = [mov.get("title") for mov in movies if mov.get("rating") == low_rated_movie.get("rating")]
# print(low_movies)

# q8) malayalam movies with genre Action

malayalam_movies_action = [mov.get("title") for mov in movies if "Action" in mov.get("genres") and "Malayalam" == mov.get("language")]
# print(malayalam_movies_action)

# q9) movies released in same years
def get_repeating_year(movies):
    for i in range(len(movies)):
        for j in range(i+1,len(movies)):
    
            if movies[i].get("year") == movies[j].get("year"):
                return movies[j].get("year")
            
repeating_year = get_repeating_year(movies)

same_year_movies = [mov.get("title") for mov in movies if repeating_year == mov.get("year")]
# print(same_year_movies)

# q10) oldest movie

oldest_movie_data = min(movies, key=get_year)
oldest_movies = [mov.get("title") for mov in movies if mov.get("year") == oldest_movie_data.get("year")]
# print(oldest_movies)

# q11) movie name with genres either Drama or Comedy

movies_filter = [mov.get("title") for mov in movies if "Drama" in mov.get("genres") or "Comedy" in mov.get("genres")]
# print(movies_filter)