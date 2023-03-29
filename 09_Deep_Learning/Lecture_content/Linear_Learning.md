# 1. Linear Learning(선형 회귀)
- `종속 변수 y`와 `한 개 이상의 독립 변수(또는 설명 변수) x` 사이의 선형 상관 관계를 모델링하는 회귀분석 기법
- 정답이 있는 데이터의 추세를 잘 설명하는 선형 함수를 찾아 x에 대한 y를 예측한다.
- 목표는 가장 적합한 $\theta$(Theta)들 값을 컴퓨터가 알아서 set을 찾아준다.
- 선형 회귀는 단순 회귀분석과 다중 회귀 분석이 있다.
- $h_o(x)=\theta_0 + \theta_1x$
- $h_o(x)=\theta_0 + \theta_1x$을 일반화시키면 $\theta_0$ + $\theta_1x_1$ + $\theta_2x_2$ + $\cdots$ + $\theta_nx_n$이 된다.

## 1. `단순 회귀분석`(Simple Regression Analysis)
- `1개`의 독립변수(x)가 1개의 종속변수(y)에 영향을 미칠 때

## 2. `다중 회귀분석`(Multivariate Regression Analysis)
- `2개 이상`의 독립변수(x)가 1개의 종속변수(y)에 영향을 미칠 때

## 3. Cost Function(비용함수)
- 예측값과 실제 값의 `차이`를 기반으로 모델의 성능(정확도)을 판단하기 위한 함수
- Linear regression의 경우 `Mean squared error function(평균 제곱 오차 함수)을 활용한다.
- 여기서 MES(Cost)가 최소가 되도록 하는 $\theta$ (parameter, a, b)를 찾아야 한다. ( $y$ = $a_x$ + $b$ )
- $b$는 $\int\limits(\theta) = \frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$
- $\int\limits(\theta)$는 에러(error)
- $h_\theta(x^{(i)})$는 예측값
- $y^{(i)}$는 정답


