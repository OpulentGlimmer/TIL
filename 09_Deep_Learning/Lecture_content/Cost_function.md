# Cost Function(비용함수)
- `예측값과 실제 값의 차이`를 기반으로 `모델의 성능(정확도)을 판단`하기 위한 함수
- Linear regression의 경우 `Mean squared error function(평균 제곱 오차 함수)을 활용한다.
- 여기서 MES(Cost)가 최소가 되도록 하는 $\theta$ (parameter, a, b)를 찾아야 한다. ( $y$ = $a_x$ + $b$ )
- $b$는 $\int\limits(\theta) = \frac{1}{m}\displaystyle\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$ 이다.
- $\int\limits(\theta)$는 `에러(error)`이다.
- $h_\theta(x^{(i)})$는 `예측값`이다.
- $y^{(i)}$는 `정답`이다.