import requests

from pprint import pprint
    
key = '69183d8d56e285cf7e7644aaff22f125'

url = 'https://api.themoviedb.org/3/movie/popular?api_key=69183d8d56e285cf7e7644aaff22f125&language=ko-KR'

data = requests.get(url).json()

def ranking():
    result = data['results']
    list_data = sorted(result, key=lambda x: x['vote_average'], reverse = True)
    return list_data[:5]

print(ranking())
