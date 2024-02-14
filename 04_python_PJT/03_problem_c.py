# 문제

## Problem C

### 특정 조건에 맞는 인기 영화 조회 II 영화목록을 평점순으로 출력하는 함수를 완성한다.

#### 1. `requests`를 이용하여 인기 영화 정보(Get Popular)에 요청을 보낸다.

#### 2. 받아온 데이터 중 평점(key `vote_average`)이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수 `ranking`을 완성한다.

from pprint import pprint

import requests

from tmdb import pre_url, key

def ranking():
    url = f'{pre_url}/movie/popular?api_key={key}'
    data = requests.get(url).json()
    result = data['results']
    list_data = sorted(result, key=lambda x: x['vote_average'], reverse = True)
    return list_data[:5]

print(ranking())
