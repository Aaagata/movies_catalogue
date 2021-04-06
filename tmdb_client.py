import requests

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular/"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(url, params=params)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movie_info(id):
    title = "https://api.themoviedb.org/3/movie/id/"
    return movie.titile

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]