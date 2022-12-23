import requests

from pprint import pprint
    
key = '69183d8d56e285cf7e7644aaff22f125'

url = 'https://api.themoviedb.org/3/movie/popular?api_key=69183d8d56e285cf7e7644aaff22f125&language=ko-KR'

data = requests.get(url).json()

def vote_average_movies():
    result = data['results']
    result_list = []

    for value in result:
        for key in result:
            if value['vote_average'] >= 8.0:
                result_list.append(value)
                break
    return result_list

pprint(vote_average_movies())