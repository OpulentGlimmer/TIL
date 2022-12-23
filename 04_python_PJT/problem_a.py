import requests
   
key = '69183d8d56e285cf7e7644aaff22f125'

url = 'https://api.themoviedb.org/3/movie/popular?api_key=69183d8d56e285cf7e7644aaff22f125&language=ko-KR'

data = requests.get(url).json()

def popular_count():
    result = data['results']
    a = len(result)
    return a

print(popular_count())

