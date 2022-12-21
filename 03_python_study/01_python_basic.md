# 파이썬

## 파이썬이란?

-  프로그래밍 언어
- 컴퓨터에게 명령할 때 쓰는 말
- 근데 컴퓨터는 0, 1밖에 모른다.
- 0, 1보다는 사람 답게 코딩하고 싶다.

 ## 코드라인

- 기본적으로 파이썬에서는 ;을 작성하지 않는다.
- 한 줄로 표기할 때는 ;을 작성하여 표기할 수 있다.
-  ;을 통해 오류를 해결하는 법
```python
print('hello');print('hello')
```

## 변수 및 자료형

### type()을 사용하는 방법
```python
name = 'amy'
print(type(name))
```
### id()를 사용하는 방법
- #### name 변수의 주소값
```python
name = 'tom'
print(id(name))
```

### 같은 값을 동시에 할당하는 방법
```python
x = 100
y = 100
print(x, y)
```
```python
x = y = 100
print(x, y)
```

### 다른 값을 동시에 할당하는 방법

#### 방법 1
```python
x, y, z = 1, 2, 3
print(x, y, z)
```
#### 방법 2
```python
x = 1
y = 2
# 여기서 y를 1로, x를 2로 바꿔보자.
# 다음 코드에 숫자는 더 이상 등장하지 않도록 한다.
# 추가 변수도 쓰지 않는다.

c = x
x = y
y = c

print(x, y)
```
#### 방법 3
```python
x = 1
y = 2
print(x, y)
x, y = y, x
print(x, y)
```

#### 방법 4
```python
x = 1
y = 2

y = x + x
x = y - x

print(x, y)
```

## 이스케이프(`\`) 시퀀스

|예약문자|내용(의미)|
|-|-|
|`\n`|줄 바꿈
|`\t`|탭|
|`\r`|캐리지리턴|
|`\0`|널(Null)|
|`\\`|\|
|`\'`|단일인용부호(')|
|`\"`|이중인용부호(")|

#### print를 하는 과정에서도 이스케이프 문자열을 활용 가능

```python
print('이건 1번줄 \n이건 2번줄에 \n쓰고 싶다.')
```
```python
print('안녕하세요', end = '')
print('반갑습니다.')
```
```python
print('안녕하세요', end = '\n')  # print함수는 end의 기본(default)값 \n 이다.
print('반갑습니다.')
```
```python
print('안녕하세요', end = '\t')
print('반갑습니다.')
```

#### 물론, end 옵션은 이스케이프 문자열이 아닌 다른 것도 가능

```python
print('안녕하세요', end='---------------')
print('반갑습니다', end='^^^^^^')
```

## String interpolation
* `%-formatting` 

* `str.format()`

* `f-strings` : 파이썬 3.6 이후 버전에서 지원

#### %-formatting을 활용
```python
name = 'amy'
print('안녕하세요 저는 %s입니다.') % name
```

```python
name = 'tom'
print('안녕하세요 저는 {}입니다.'.format(name))
```

```python
print(f'안녕하세요 저는 {name}입니다.')
```

##  다양한 형식을 활용하기 위해 datetime 모듈로 오늘을 표현

```python
import datetime
today = datetime.datetime.now()  # = 은 할당, 오른쪽은 값
print(today)
```

## string interpolation에서 연산과 숫자 출력형식을 지정

```python
import datetime
today = datetime.datetime.now()
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}요일입니다.')
```

```python
import datetime
today = datetime.datetime.now()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일 {today:%A}요일입니다.')
```

```python
import datetime
pi = 3.141592
print(f'원주율은 {pi}입니다. 반지름 2원의 넓이는 {pi * 2 * 2}')
```

## 단축평가
- 첫 번째 값이 확실할 때, 두 번째 값은 확인 하지 않음
- 조건문에서 뒷 부분을 판단하지 않아도 되기 때문에 속도 향상

- and 는 둘 다 True일 경우만 True이기 때문에 첫번째 값이 True라도 두번째 값을 확인해야 하기 때문에 'b'가 반환된다.

```python
print(1 and 2 and 0 and 4)  # 1, 2, 4는 True, 0은 False 따라서 결과값은 0
```

```python
print(True and True and False and True)  # 결과값은 False
```

```python
print(1 and 0)  # 1은 True이고, 0은 False 따라서 결과값은 0
```

```python
print(0 and '')  # 0은 False이고 ''은 True이므로 결과값은 ''
```

- or 는 하나만 True라도 True이기 때문에 True를 만나면 해당 값을 바로 반환한다.

```python
print('a' or 'b')  # bool값으로 반환하면 'a'는 True 이다.
```

```python
print(0 or 1)  # 0은 False, 1은 True이므로 결과값은 1
```

```python
print(10 or 11)  # 10은 True이므로 결과값은 10
```

## 복합연산자
- 복합 연산자는 연산과 대입이 함께 이루어 진다.
- 가장 많이 활용되는 경우는 반복문을 통해서 개수를 카운트하거나 할 때 활용된다.

#### 복합연산자는 이럴 때 사용

```python
num = 0
num = num + 1
```

```python
num = 0

while num < 5:  # num 이 5보다 작을 동안
    print(num)  # num 출력
    num = num + 1  # num +=1
# 결과값은 0, 1, 2, 3, 4
```

```python
num = 0

while num < 5:  # num 이 5보다 작을 동안
    num = num + 1  # num +=1
    print(num)  # num 출력
# 결과값은 1, 2, 3, 4, 5
```

## 기타 연산자

- Concatenation : 연속적으로 붙이다.
- 숫자가 아닌 자료형은  `+` 연산자를 통해 합칠 수 있습니다.

#### 문자열 더하기
```python
print('py' + 'thon')
# 결과값은 'python'
```
```python
print([1, 2] + [3, 4])
# 결과값은 [1, 2, 3, 4]
```

## Containment Test
- `in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있습니다.
  
#### 문자열안에 특정한 문자가 있는지 확인

```python
print('a' in 'aeiou')
# 결과값은 True
```

```python 
print('b' in 'asdf')
# 결과값은 False
```

#### list안에 특정한 원소가 있는지 확인
```python
print(1 in [4,  3, 1, 2, 3])
# 결과값은 True
```

```python
print(100 in [4,  3, 1, 2, 3])
# 결과값은 False
```

#### range안에 특정한 원소가 있는지 확인

```python
print(1 in range(10))
# 결과값은 True
```

```python
print(11 in range(10))
# 결과값은 False
```

```python
print(10 in range(10))
# 결과값은 False
```

```python
print(1.1 in range(10))
# range는 1부터 9까지 정수로만 되어있어서 결과값은 False
```
## Identity

- `is` 연산자를 통해 동일한 object인지 확인

#### 파이썬에서 -5 부터 256 까지의 id는 동일
```python
a = 3
b = 3
print(id(a), id(b))  # 많이 쓰는 값이라서 미리 메모리의 활당하는게 좋아서이다.
# 결과값 id(a)와 id(b) id는 같다.
```

```python
a = 'a'
b = 'a'
print(id(a), id(b))  # 영어도 있다.
# 결과값 id(a)와 id(b) id는 같다.
```
#### 257 이루의 id 는 다르다.
```python
a = 257
b = 257
print(id(a), id(b))
# 결과값 id(a)와 id(b) id는 다르다.
```
```python
a = '가'
b = '가'
print(id(a), id(b))
# 결과값 id(a)와 id(b) id는 다르다.
```
## Indexing/Slicing

- `[]`를 통한 값을 접근
- `[:]`을 통해 리스트를 슬라이싱할 수 있다.

```python
s = 'abc'
print(s[0])
# 결과값은 'a'이다.
```
```python
s = 'python'
print(s[4])
# 결과값은 'o'이다.
```

```python
s = 'python'
print(s[-1])
# 결과값은 'n'이다.
```

```python
s = 'python'
print(s[-2])
# 결과값은 'o'이다.
```

```python
s = 'python'
print(s[2:6])# 2이상부터 6미만까지
# 결과값은 'thon'이다.
```

## 명시적 형변환

### 모두 명시적으로 형 변환을 해 주어야 한다.
- string -> intger : 형식에 맞는 숫자만 가능
- integer -> string : 모두 가능
### 암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능
- int() : string, float를 int로 변환
- float() : string, int를 float로 변환
- str() : int, float, list, tuple, dictionary를 문자열로 변환
```python
print(2 + int('6'))  # string 6을 integer로 변환
# 결과값은 8
```
```python
print(int('qaxc'))  # int('qaxc') => 불가능
# 결과는 오류남
```
```python
print(int('2.1'))  # string '2.1'를 float로 변환
# 결과는 2.1
```
```python
a ='asdf'
print(int(a))
# string은 글자가 숫자일때만 형변환이 가능
# 결과는 오류남
```
```python
print(int(2.1))
# string 2.1를 int로 변환할 수는 없다.
```

## 시퀀스
- 시퀀스는 데이터가 순서대로 나열된 형식
- 주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.
  
### 기본적인 시퀀스 타입
- 리스트(list)

- 튜플(tuple)

- 레인지(range)

- 문자열(string)

- 바이너리(binary) : 따로 다루지는 않는다.

## list(리스트)
- 활용법 : [value1, value2, value3]
- 리스트는 대괄호[] 및 list() 를 통해 만들 수 있다.
- 값에 대한 접근은 list[i]를 통해 한다.

### 빈 리스트 만들기
#### 방법 1
```python
q =[]
print(q)
```
#### 방법 2
```python
ql = list()
print(ql)
```

### 원소를 포함한 리스트 만들기
-  list는 복수형 단어로 하고, 띄어 쓰기 꼭 지키기
  ```python
  locations = ['강남', '서초', '송파', '광진', '마포',]  # 복수형이면 끝에 s를 붙인다.
  ```

```python
numbers = [
    1,
    2,
    3,
    4,
    5,
    6,  # trailing comma(따라오는 컴마) # 모든지 마지막에 ,(컴마)를 찍어준다.
]
print(numbers)
# 결과값은 [1, 2, 3, 4, 5, 6]
```
#### 리스트 슬라이싱하는 방법
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
print(location[0])
# 결과값은 강남
```
#### 리스트 값을 변경할 때
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations[0] = '양천'
print(locations)
# 결과값은 ['양천', '서초', '송파', '광진', '마포']
```
#### 리스트 값을 추가할 때
- string값을 리스트에 추가할 때
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations.append('동탄')
print(locations)
# 결과값은 ['양천', '서초', '송파', '광진', '마포', '동탄']
```

- int값을 리스트에 추가할 때
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations.append(1)
print(locations)
# 결과값은 ['강남', '서초', '송파', '광진', '마포', 1]
```

- 논리값을 리스트에 추가할 때
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations.append(True)
print(locations)
# 결과값은 ['강남', '서초', '송파', '광진', '마포', True]
```

- 리스트를 리스트에 추가할 때
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations.append([1, 2, 3])
print(locations)
# 결과값은 ['강남', '서초', '송파', '광진', '마포', [1, 2, 3]]
```

- 리스트 5번째에 있는 [1]을 [2]로 바꿀 때
```python
locations = ['강남', '서초', '송파', '광진', '마포', [1], '동탄', 1, True, [1, 2, 3]]
locations[5] = [2]
locations
# 결과값은 ['강남', '서초', '송파', '광진', '마포', [2], '동탄', 1, True, [1, 2, 3]]
```

- 리스트에서 '서'만 출력하고 싶을 때
```python
locations = ['강남', '서초', '송파', '광진', '마포', [1], '동탄', 1, True, [1, 2, 3]]
locations[1][0]
# 결과값은 서
```

## tuple(튜플)
- 활용법 : (value1, value2)
- 튜플은 리스트와 유사하지만, ()로 묶어서 표현
- tuple은 수정 불가능(불변, immutable)하고, 읽을 수 밖에 없다.
- 직접 사용하기 보다는 파이썬 내부에서 사용하고 있다.
####  튜플에는 값을 바꿀 수 없다.
```python
tt = (1, 2, 3)
tt[1] = 100
# 결과값은 오류가 난다.
```
#### 빈 튜플은 빈 괄호 쌍으로 만들어진다.
```python
t =()
print(t)
# 결과값은 ()
```
#### # 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만든다.
```python
w = (1, )
print(w)
# 결과값은 (1,)
```

## range()
- `range` 는 숫자의 시퀀스(순서를 나타냄)를 나타내기 위해 사용
  
#### 기본형 : range(n)

- 0부터 n-1까지 값을 가짐

#### 범위 지정 : range(n, m)

- n부터 m-1까지 값을 가짐

#### 범위 및 스텝 지정 : range(n, m, s)

- n부터 m-1까지 +s만큼 증가한다

#### range()를 이용해서 숫자 1개만 뽑는 방법
```python
import random

numbers = range(1, 6)  # 1개만 뽑기
random.choice(numbers)
# 결과값은 random하게 하나만 뽑아진다.
```
#### range()를 이용해서 숫자 n개 뽑는 방법
```python
import random

numbers1 = range(1, 6)  # n개 뽑기
random.sample(numbers, 2)
# 결과값은 random하게 숫자 2개 뽑아진다.
```
#### range()를 이용해서 로또복권 6자리 숫자 뽑는 방법
```python
import random

numbers = range(1, 46)
lucky = random.sample(numbers, 6)
lucky.sort()  # sort()는 정렬할 때 쓰임
print(lucky)
# 결과값은 6자리 숫자 random하게 뽑아짐
```

#### range에 담긴 값을 list로 바꿔서 확인하는 방법
```python
print(list(range(1)))
# 결과값은 [0]
```

```python
print(list(range(0, 1)))
# 결과값은 [0, 1]
```

#### 4 ~ 8까지의 숫자를 담은 range를 만드는 방법
```python
r1 = range(4, 9)
print(list(r1))
# 결과값은 [4, 5, 6, 7, 8]
```

#### 0부터 -9까지 담긴 range를 만드는 방법
```python
r2 = range(-9, 1)
print(list(r2))
# 결과값은 [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
```

##### range() 첫번째에는 시작하는 숫자, 두번째에는 끝나는 숫자에 -1 숫자, 세번째에는 입력한 숫자만큼 증가하는 숫자를 넣는다. 

```python
r2 = range(0, -10, -1)
print(list(r2))
# 결과값은 [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```

```python
r3 = range(0, 20, 3)
print(list(r3))
# 결과값은 [0, 3, 6, 9, 12, 15, 18]
```

## 시퀀스에서 활용할 수 있는 연산자/함수

|operation|설명|
|-|-|
|x in s|containment test|
|x not in s|containment test|
|s1 + s2|concatenation(연결, 연쇄)|
|s * n|n번 만큼 반복하여 더하기|
|s[i]|indexing|
|s[i:j]|slicing|
|s[i:j:k]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

### contain test를 확인
```python
s = 'string'
'a' in s  # 'a'라는 것이 s에 있다.
# 결과값은 False
```

```python
r = [1, 2, 3, 4, 5]
2 in r  # 2라는 값이 r안에 있다.
```
### concatenation(연결, 연쇄)
```python
print('안녕' + '하세요')
# 결과값은 안녕하세요
```

```python
print([1, 2] + [3, 4])
# 결과값은 [1, 2, 3, 4]
```

### s * n	n번만큼 반복하여 더하기
```python
print([0] * 6)
# 결과값은 [0, 0, 0, 0, 0, 0]
```

### indexing과 slicing
```python
locations = ['강남', '서초', '송파', '광진', '마포',]
locations[1:3]  # 두번째, 세번째 값만 가져오기
# 결과값은 ['서초', '송파']
```

#### list[`x:y`] => idx `x` ~ idx `y-1`, `step 1`
#### list[`x:y:z`] => idx `x` ~ idx `y-1`, `step z`
#### list[`x::z`] => idx `x` ~ `끝까지` `step z`
#### list[`::z`] => `처음부터 끝까지` `step z`
#### list[`x:y:`] => idx `x` ~ idx `y-1` `step 1`
#### list[`::`] => `그대로`(idx `x` ~ idx `y-1`, `step 1`을 의미)

```python
numbers = list(range(0, 31))
numbers[0::3]
# 결과값은 [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```

### list 길이 확인하는 방법
```python
numbers = list(range(0, 31))
numbers[0::3]
len(numbers)  # list를 만든 길이 확인
# 결과값은 11
```

### list 길이 최솟값 확인하는 방법
```python
numbers = list(range(0, 31))
numbers[0::3]
min(numbers)  # list를 만든 최솟값 확인
# 결과값은 0
```
### list 길이 최댓값 확인하는 방법
```python
numbers = list(range(0, 31))
numbers[0::3]
max(numbers)  # list를 만든 최댓값 확인
# 결과값은 30
```

### list에 담긴 특정한 것의 개수를 확인

```python
min('aA!bB')
# 결과값은 !
```

## set
- `set`은 순서가 없는 자료구조
- 세트는 수학에서의 집합과 동일하게 처리된다.

- 세트는 중괄호{}를 통해 만들며, 순서가 없고 중복된 값이 없다.

- 빈 집합을 만들려면 set()을 사용해야 합니다. {}로 사용 불가능.
- 활용법 : `{value1, value2, value3}`

|연산자/함수|설명|
|-|-|
|a `-` b|차집합|
|a `\|` b|합집합|
|a `&` b|교집합|
|a`.difference(b)`|차집합|
|a`.union(b)`|합집합|
|a`.intersection(b)`|교집합|

#### set 두개를 만들어서 연산자들을 활용하는 방법
- a `-` b 차집합
```python
set1 = {1, 2, 3}
set2 = {3, 6, 9}

print(set1-set2)
# 결과값은 {1, 2}
```
- a `|` b 합집합
```python
set1 = {1, 2, 3}
set2 = {3, 6, 9}

print(set1 | set2)
# 결과값은 {1, 2, 3, 6, 9}
```

- a `&` b 교집합
```python
set1 = {1, 2, 3}
set2 = {3, 6, 9}

print(set1 & set2)
```

### set은 중복된 값이 있을 수 없다.
```python
set3 = {1, 1, 1, 1, 1}
print(set3)
# 결과값은 {1}
```

#### set으로 중복된 값을 제거
```python
numbers = [1, 2, 3, 3, 2, 4, 1, 1]
uniq = []
for number in numbers:
    if number not in uniq:
        uniq.append(number)
print(uniq)
# 결과값은 [1, 2, 3, 4]
```

```python
numbers = [1, 2, 3, 3, 2, 4, 1, 1]
list(set(numbers))
# 결과값은 [1, 2, 3, 4]
```

## dictionary

- `dictionary`는 아이템이 삽입되는 순서를 가지고 있다.
- 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다. 
- `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
- `key`는 불변(immutable)한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.
- 활용법 : `{Key1:Value1, Key2:Value2, Key3:Value3, ...}`

### 비어있는 dictionary 만들기
```python
dict_a = {}
dict_a
# 결과값은 {}
```
```python
dict_b = dict()
dict_b
# 결과값은 {}
```

### dictionary는 중복된 key는 존재할 수가 없다.
```python
d = {'a': '에이', 'b': '삐', 'a': '에에이'}
d
# 결과값은 {'a': '에에이', 'b': '삐'}
```

### 지역번호(서울-02 경기-031)가 담긴 전화번호부를 만드는 방법
```python
phone_book = {'서울': '02', '경기': '031',}
print(phone_book)
# 결과값은 {'서울': '02', '경기': '031'}
```

### 딕셔너리는 슬라이싱할 때 키 값을 쓴다.
```python
phone_book = {'서울': '02', '경기': '031',}
print(phone_book['서울'])
# 결과값은 02
```
### 테이블 만들 때
```python
[
    {'이름': 'amy', '전공': '행정학', '성별': '여자',},
    {'이름': 'tom', '전공': '경영학', '성별': '남자',}
]
```

### 딕셔너리의 .keys() 메소드를 활용하여 key를 확인해 볼 수 있다.
```python
phone_book = {'서울': '02', '경기': '031',}
phone_book.keys()
# 결과값은 dict_keys(['서울', '경기'])
```

### 딕셔너리의 .values() 메소드를 활용하여 value를 확인해 볼 수 있다.
```python
phone_book = {'서울': '02', '경기': '031',}
phone_book.values()
# 결과값은 dict_values(['02', '031'])
```

### 딕셔너리의 .items() 메소드를 활용하여 key, value를 확인해 볼 수 있다.
```python
phone_book = {'서울': '02', '경기': '031',}
phone_book.items()
# 결과값은 dict_items([('서울', '02'), ('경기', '031')])
```
### 딕셔너리의 value 바꾸기
```python
phone_book = {'서울': '02', '경기': '031',}
phone_book['경기'] = '033'
phone_book
#  결과값은 033
```

#### 딕셔너리의 key - value 추가하기
```python
phone_book = {'서울': '02', '경기': '031',}
phone_book['부산'] ='051'
phone_book
# 결과값은 {'서울': '02', '경기': '031', '부산': '051'}
```