import requests

from pprint import pprint

def recommendation(title):
    
    key = '69183d8d56e285cf7e7644aaff22f125'

    url = f'https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-KR&query={title}&page=1&include_adult=false'

    data = requests.get(url).json()

    result = data['results']
    
    if result == []:

        return None
    
    else:

        id = result[0]['id']

        urll = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=69183d8d56e285cf7e7644aaff22f125&language=en-US&page=1'

        data_two = requests.get(urll).json()

        result_two = data_two['results']
        
        lists = []
        
        for idx in range(len(result_two)):
            
            lists.append(result_two[idx]['title'])
            
        return lists

pprint(recommendation('기생충'))

pprint(recommendation('그래비티'))

pprint(recommendation('검색할 수 없는 영화'))