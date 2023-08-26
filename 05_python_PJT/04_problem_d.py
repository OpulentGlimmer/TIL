# 문제

## Problem D

### 특정 영화 추천 영화 조회 제공된 영화 제목을 기준으로 추천영화 목록을 출력한다.

#### 1. `requests`를 이용하여 영화 검색(Search Movies) 요청을 보낸다. (인자로 넘어온 `title` 사용)
#### 2. 결과중 첫번째 영화가 검색한 영화가 맞다면 해당 영화의 id를 사용한다.
#### 3. id를 기반으로 추천영화 목록 조회 (Get Recommendations) URL을 생성한다. 
#### 4. `requests`를 이용하여 추천영화 목록 조회 URL에 요청을 보낸다. 
#### 5. 추천받은 영화 리스트에서 **제목만을** 리스트에 저장한다. 
#### 6. 저장된 리스트를 반환하는 함수 `recommendation`을 완성한다. 
#### 7. (2번) id값은 있지만 추천영화가 없는 경우 빈 리스트를 반환한다. 
#### 8. (3번) 올바르지 않은 영화 제목으로 검색할 수 없는 경우 `None`을 반환한다. 

from pprint import pprint

import requests

from tmdb import pre_url, key

def recommendation(title):
    
    url = f'{pre_url}/search/movie?api_key={key}&query={title}&language=ko-KR'

    data = requests.get(url).json()

    result = data['results']
    
    if result == []:

        return None
    
    else:

        id = result[0]['id']

        url = f'{pre_url}/movie/{movie_id}/recommendations?api_key={key}&language=ko-KR'

        data_two = requests.get(urll).json()

        result_two = data_two['results']
        
        lists = []
        
        for idx in range(len(result_two)):
            
            lists.append(result_two[idx]['title'])
            
        return lists

pprint(recommendation('기생충'))

pprint(recommendation('그래비티'))

pprint(recommendation('검색할 수 없는 영화'))