import requests, json

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

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(endpoint, params=params)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(endpoint, params=params)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(endpoint, params=params)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()

def get_lists():
    endpoint = "https://api.themoviedb.org/3/list/{list_id}"
    params = {'api_key': "b1d1fa80c18bfb8de4dc513c02c952a4"}
    response = requests.get(endpoint, params=params)
    return response.json()