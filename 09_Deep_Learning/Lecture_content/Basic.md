# 1. 인공지능 적용하기
- 회사를 소개할 때 우리 회사는 어떤 데이터를 활용하여, 어떤 모델을 만들고, 이 모델을 적용한 어떤 기능을 만드는 회사라고 설명을 할 줄 알아야 한다.
- 어떤 `모델`을 만들 것인가? = `뛰어난 기술`로부터 출발할 것인가?를 찾아야 한다.
- 어떤 `기능`을 만들 것인가? = `고객의 Needs`로부터 출발할 것인가?를 찾아야 한다.
- 따라서 인공지능을 적용한다는 것은 `문제 해결을 위한 도구로서의 인공지능 기술을 적용`을 말한다.

# 2. 모델(Model)이란? 
- 통계학 모형에서 유래 : x가 들어가서 계산한 다음에 y라는 결과가 나오는 구조
- 데이터를 설명할 수 있는 것
- $y=a_x+b$ 이다.
- $a$과 $b$를 (모델의) Parameter, $\theta$(쎄타)라고 한다.

---
|이름|설명|
|--|--|
|$y$|(모델의) 예측값|
|$a$|기울기|
|$_x$|데이터|
|$b$|y절편|
---

# 3. 학습(Learning)이란?
- 내 데이터에 맞는 모델을 찾는 과정 = 모델 적합(`Model fitting`)
- 내가 다루고 있는 `데이터를 가장 잘 설명하는 방법`을 찾는 과정
- 실제 정답과 예측 결과 사이의 오차(Loss, Cost, Error)를 줄여나가는 최적화 과정이다.
  
---

# 4. 데이터를 가장 잘 설명하는 모델 찾는 방법
- 최적화하는 과정은 아래와 같다.
  
- 1. 초기 모델(가설 모델)에 데이터를 넣는다.
- 2. 결과를 `평가`한다.(예측/분류의 정확도 등 = mean squared error, classification error, recall & precision, etc 활용)
- 3. 결과를 개선하기 위해 `모델`을 수정한다.(모델 내부의 Parameter($\theta$ 쎄타 파라미터(Parameter))수정, 모델 종류의 변경 등)

---

# 5. Model Capacity
- 모델의 포용력, 용량을 말한다.
- 모델이 복잡해질수록 Capacity는 커지면 overfitting발생할 경우도 커진다.
- Capacity 극대화하면 Overfitting발생한다.
- Overfitting이 있으면 Generalization error(일반화 에러/성능)가 증가한다.
- Generalization error(일반화 에러/성능)란 새로운 데이터에 적용했을 때 보이는 에러를 말한다.
- Generalization error(일반화 에러/성능)가 있으면 새로운 데이터에 잘 대응하지 못하게 된다.

---

# 6. Cross validation(교차검증)
- 데이터를 Training data모델 70%, Validation data모델 15%, Test data모델 15% 3개의 그룹으로 나눈다.
- 1. Training data모델 70% 학습시킨다.
- 2. Validation data모델 15%(or Hyper Parameter)을 최적화/선택(Tune)한다.
- 3. Test data모델 15% 평가(Test only, no mire tune)한다.
  
---

# 7. 그 외 활용되는 것들
|방법|설명|
|:-----:|:-----:|
|Cost function에 Regularization term 추가|L1 or L2, ,weight up = cost up|
|(Stratified) K-fold crossvalidation|후보 모델 간 비교 선택을 위한 알고리즘|
|Drop-out & Batch Normalization 등|(NN 등)|

---

# 8. Data augmentation
- 이미지, 음성, 텍스트 데이터 기준으로 예를 들어서 1만 데이터가 있다면 그 데이터를 살짝 수정해서 10만장 만드는 작업을 들 수 있다.
---

# 9. 새로운 데이터들에 대해서 좋은 결과가 나오게 하는 방법
- training data를 많이 확보하거나 모델의 Feature를 줄이는 것도 좋은 방법이다.
  
- 이미지, 음성, 텍스트 데이터 기준으로 1만 데이터 살짝 수정해서 10만장 만드는 것을 말한다.






  