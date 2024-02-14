# 01_Numpy_Basic

- python 코드 
```python
import numpy as np  # numpy 라이브러리 호출

a = [1, 2, 3]  # a는 일반 list 이다.

b = np.array(a)  # b는 ndarray이다.
```

## array 생성
```python
l1 = [4, 5, 6]

array_l1 = np.array(l1)
```

## type과 shape을 확인
```python
# 타입(type) 확인
print('array_l1 type:', type(array_l1))

# 형태(shape) 확인
print('array_l1 shape:', array_l1.shape)
```

## 1차원 자료 생성
- python 코드
```python
array1d = np.array([1, 2, 3])

# 타입(type) 확인
print('array1d 타입:', type(array1d))

# 형태(shape) 확인

# 한 요소를 추출하는데 필요한 최소 첨자수가 한 개이다.
# 결과가 (3, )으로 나오는데 앞에 3은 리스트에 안에 있는 숫자의 갯수를 말한다.
# 리스트가 한 개이므로 (3, )으로 결과가 나온다.
print('array1d 형태:', array1d.shape)

# 차원 확인(ndim 함수는 몇 차원인지 알 수 있는 함수)
print('array1d는 {0}차원'.format(array1d.ndim))
```

- 결과
```
array1d 타입: <class 'numpy.ndarray'>

array1d 형태: (3,)

array1d는 1차원
```

## 2차원 자료 생성
- python 코드
```python
array2d = np.array([[1, 2, 3], 
                  [11, 22, 33]])

# 타입(type)확인
print('array2d type:', type(array2d))

# 형태(shape)확인
# [1, 2, 3]과 [11, 22, 33] 리스트 안에 있는 값이 3개이므로 결과값(2, 3)중에 3이 의미한 것이다.
# [[1, 2, 3], [4, 5, 6]]으로 리스트가 두 개인데 데이터가 [1, 2, 3]과 [4, 5, 6]이 두 개 있어서 결과값(2, 3)중에 2를 의미한다.
print('array2d의 형태:', array2d.shape)

# 차원 확인(ndim 함수는 몇 차원인지 알 수 있는 함수)
print('array2d는 {0}차원'.format(array2d.ndim))
```

- 결과
```
array2d type: <class 'numpy.ndarray'>

array2d의 형태: (2, 3)

array2d는 2차원
```

# 3차원 자료 생성
- python 코드
```python
array3d = np.array([[[1, 2, 3], 
                  [11, 22, 33]]])

# 타입(type)확인
print('array3d type:', type(array3d))

# 형태(shape)확인
# [1, 2, 3]과 [11, 22, 33] 리스트 안에 있는 값이 3개이므로 결과값(1, 2, 3)중에 3이 의미한 것이다.
# [[[1, 2, 3], [4, 5, 6]]] 리스트가 세 개인데 데이터가 [1, 2, 3]과 [4, 5, 6]이 두 개 있어서 결과값(1, 2, 3)중에 2를 의미한다
# [[[1, 2, 3], [4, 5, 6]]] 바깥에 있는 리스트 안에 있는 데이터가 [[1, 2, 3], [4, 5, 6]] 한 개이므로 결과값(1, 2, 3)중에 1을 의미한다.
print('array3d의 형태:', array3d.shape)

# 차원 확인(ndim 함수는 몇 차원인지 알 수 있는 함수)
print('array3d는 {0}차원'.format(array3d.ndim))
```

- 결과
```
array3d type: <class 'numpy.ndarray'>

array3d의 형태: (1, 2, 3)

array3d는 3차원
```

# 결과값 [1, 2, 3, 4, 5, 6]으로 나타내는 코드
- python 코드
```python
x = [1, 2, 3]
y = [4, 5, 6]

print(x+y)
```

# 결과값 [5, 7, 9]으로 나타내는 코드
- python 코드
```python
array_x = np.array(x)
array_y = np.array(y)

print(list(array_x+array_y))
```

# ?을 활용한 함수 검색
- python 코드
```python
?np.array
?np.shape
?np.ndim
```

# help 함수를 통한 검색
- python 코드
```python
help(np.ndim)
```

# reshape 용례

## 1. arange

```python
np.arange(start=1, stop=11)
```

- 결과
```
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```
- python 코드
```python
seq_array = np.arange(1, 11)

# dtype확인
print(seq_array.dtype)

# 형태(shape)확인
print(seq_array.shape)
```

- 결과
```
# dtype확인
int32

# 형태(shape)확인
(10,)
```

## zeros 로 0으로 된 행렬 생성
- python 코드
```python
np.zeros((3, 2), dtype='int32')
```

- 결과
```
array([[0, 0],
       [0, 0],
       [0, 0]])
```
- python 코드
```python
zero_array = np.zeros((3, 2), dtype='int32')
print(zero_array.shape)
```

- 결과
```
# 형태(shape)확인
(3, 2)
```

## ones 로 1로 된 행렬 생성

- python 코드
```python
np.ones((3, 2), dtype='int32')
```

- 결과
```
array([[1, 1],
       [1, 1],
       [1, 1]])
```

- python코드
```python
one_array = np.ones((3, 2), dtype='int32')

# dtype확인
print(one_array.dtype)

# 형태(shape)확인
print(one_array.shape)
```

- 결과
```
# dtype확인
int32

# 형태(shape)확인
(3, 2)
```

## reshape

- python코드
```python
seq_array = np.arange(1, 11)
seq_array21 = seq_array.reshape(2, 5)
seq_array21
```

- 결과
```
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])
```

- python 코드
```python
# 형태(shape)확인
seq_array21.shape
```

- 결과
```
# 형태(shape)확인
(2, 5)
```

- python 코드
```python
# -1은 자동으로 나머지의 행이나 열이 들어간다.
seq_array31 = seq_array.reshape(-1, 5)
seq_array31
```

- 결과
```
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])
```

- python 코드
```
# 형태(shape)확인
seq_array31.shape
```

- 결과
```
# 형태(shape)확인
(2, 5)
```