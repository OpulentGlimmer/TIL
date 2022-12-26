# 문제

## Problem A

### 인기 영화 조회 인기 영화의 개수를 출력한다.

#### 1. `requests`를 이용하여 인기 영화 정보(Get Popular)에 요청을 보낸다.

#### 2. popular를 기준으로 받아온 데이터에서 영화 리스트의 개수를 계산한다.

#### 3. 계산한 정보를 반환하는 함수 `popular_count`를 완성한다.

import requests
from tmdb import pre_url, key

def popular_count():
    url = f'{pre_url}/movie/popular?api_key={key}'
    data = requests.get(url).json()
    result = data['results']
    return len(result)

print(popular_count()) 

