# Python - Data 수집 프로젝트



## 준비사항 

### 사용 API

-  TMDB API(https://developers.themoviedb.org/3) 

### 개발언어/프로그램 

- Python 3.9 이상 
- 아래중 택1
  - VS code
  - Jupyter notebook

### 필수 라이브러리 

- `requests ` 

  ```sh
  $ pip install requests
  ```



### `requests` 사용법

```python
import requests  # requests 모듈 호출

res = requests.get(URL)  # URL 로 요청 보냄

data = res.json()  # 요청의 응답 JSON을 *dict*로 변환함

print(data)  # data 확인(list or dict일 확률이 높음)
```



