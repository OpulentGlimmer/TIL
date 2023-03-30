# Neural Network Optimization method 1 (신경망 최적화 방법 1)
# 1. 가중치 초기화(Weight lnitialization)
![alt text](./Picture/Gradient_Descent_Algorithm.png)
- Gradient Descent(경사 하강법)를 적용하기 위한 첫 단계는 모든 $\theta$를 초기화하는 것이다.
- 초기화 시점의 작은 차이가 학습의 결과를 뒤바뀔 수 있으므로 보다 나은 초기화 방식을 모색할 수 있다.

---
- `Perceptron의 선형결합(Linear combination)결과값(=활성화 함수(Activation function으로의 입력값)이 너무 커지거나 작아지지 않게 만들어지는 것이 핵심`이다.

## 1. Use Xavier(자비에 or 이그재비어 or 세이비어) lnitialization
- 활성화 함수(Activation function)로 `시그모이드 함수(Sigmoid function)`나 `탄 함수(tanh function)`를 사용할 때 사용한다.
- 다수의 딥러닝 라이브러리에 `Default로 적용`되어 있다.
- 표준편차가 $\sqrt\frac{1}{n}$인 정규분포를 따르도록 가중치를 초기화한다.
- 여기서 $n$은 # of nodes of previous layer(이전 레이어의 노드 수)를 의미한다.

## 2. He Initialization
- 활성화 함수(Activation function)가 `ReLU함수`일 때 적용한다.
- 표준편차가 $\sqrt\frac{2}{n}$인 정규분포를 따르도록 가중치를 초기화한다.

## 3. 부록

### `시그모이드함수(Sigmoid function)` 의미
**  $a(x)$ = 1 / (1 + $e^{-x}$)

![alt text](./Picture/Sigmoid_function.png)

- 시그모이드 함수(Sigmoid function)는 0에서 1 사이의 함수이며, 값이 들어왔을 때, 0~1 사이의 값을 변환한다.
- 시그모이드 함수(Sigmoid functon)를 활성화 함수(Activation function)로 사용하면, 0과 1로 가까운 값을 통해 `이진분류`를 할 수 있다.
- 연속형 데이터이기 때문에, 계단 함수가 끊기지 않는 매끄러운 모양으로 바뀐다.
- 동시에 이상치가 들어온다 할지라도, 시그모이드 함수는 0과 1로 수렴하므로, 이상치 문제가 해결되면서 연속된 값을 전달할 수 있다.

### `시그모이드함수(Sigmoid function)` 장점

- 분류는 0과 1로 나뉘며, `출력 값이 어느 값에 가까운지를 통해 어느 분류에 속하는지 쉽게 알 수 있다.
- 출력값의 범위가 0~1 사이이며, 매우 매끄러운 곡선을 가지고 있어서, 경사하강법(Gradient Descent)을 실행 할 때 기울기가 급격하게 변해서 발산하는 기울기 폭주(Gradient Exploding)가 발생하지 않는다.

### `시그모이드함수(Sigmoid function)` 단점

- 핵심 : 기울기 소실 문제, 학습 속도 저하 문제 발생

1. 기울기 소실 문제(Gradient Vanishing)

- 입력값이 아무리 크더라도, 출력되는 값의 범위가 매우 좁기 때문에 경사하강법(Gradient Descent) 실행한 경우에 범위가 너무 좁아서, 0에 수렴하는 기울기 소실(Gradient Vanishing)이 발생할 수 있다.
- 출력 값의 중앙값이 0이 아닌 0.5이며, 모두 양수이기 때문에 출력의 가중치 합이 입력의 가중치합보다 커지게 되는데 이를 `편향 이동(Bias Gradinet)라고 한다.
- 신호가 각 레이어를 통하게 할 때마다 분산이 계속 커지게 되어, 활성화 함수(Activation function)의 출력이 최댓값과 최솟값이 0과 1에 수렴하게 된다.
- 0이나 1에 가까울수록 당연히 출력되는 값이 0에 가까워지게 되는데, 이로 인해 뉴런의 기울기(Gradient)값이 0이 된다.
- 역전파 시 0이 곱해져서 기울기가 소멸(kill)되는 현상이 발생해 버리는 것(역전파가 진행될수록 아래 층(Layer)에 아무런신호가 전달되지 않는 것)을 기울기 소실(Gradient Vanishing)라고 한다.

2. 학습 속도 저하 문제
- 시그모이드 함수의 출력값은 모두 양수기 때문에 경사하강법을 적용할 때, 그 기울기가 양수거나 음수가 한다.
- 이는 기울기 업데이트가 지그재그로 변동하는 결과를 가지고 오고, 학습 효울성을 감소시켜 학습에 더 많은 시간이 들어가게 만든다.

### 결론
- 출력층에서 시그모이드 함수(Sigmoid function)를 사용하는 것은 상관없으나, 아래로 정보가 계속 흘러가는 은닉층(Hidden layer)에서는 시그모이드 함수를 활성화 함수(Activation function)로 사용해서는 안 된다.
- 즉, 시그모이드 함수(Sigmoid function)는 이진 분류를 하고자 하는 경우 출력층에서만 사용하는 것을 권장한다.
