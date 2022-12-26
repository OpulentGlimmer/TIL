# 문제

## Problem B

###  Problem A에서 popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력한다.

#### 1. `requests`를 이용하여 인기 영화 정보(Get Popular)에 요청을 보낸다.

#### 2. 받아온 데이터에서 평점(key `vote_average`)를 기준으로 점수가 8 이상인 영화들의 목록을 리스트로 반환하는 함수 `vote_average_movies`를 완성한다.

from pprint import pprint

import requests
from tmdb import pre_url, key

def vote_average_movies():
    url = f'{pre_url}/movie/popular?api_key={key}'
    data = requests.get(url).json()
    result = data['results']
    result_list = []

    for value in result:
        for key in result:
            if value['vote_average'] >= 8.0:
                result_list.append(value)
                break
    return result_list

pprint(vote_average_movies())