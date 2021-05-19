# [신용카드 사용자 연체 예측 AI 경진대회](https://dacon.io/competitions/official/235713/overview/description)

## [데이터 변수 설명](https://www.dacon.io/competitions/official/235713/talkboard/402821/)
- index
- gender: 성별
- car: 차량 소유 여부
- reality: 부동산 소유 여부
- child_num: 자녀 수
- income_total: 연간 소득
- income_type: 소득 분류
  - ['Commercial associate', 'Working', 'State servant', 'Pensioner', 'Student']
- edu_type: 교육 수준
  - ['Higher education' ,'Secondary / secondary special', 'Incomplete higher', 'Lower secondary', 'Academic degree']
- family_type: 결혼 여부
  - ['Married', 'Civil marriage', 'Separated', 'Single / not married', 'Widow']
- house_type: 생활 방식
  - ['Municipal apartment', 'House / apartment', 'With parents', 'Co-op apartment', 'Rented apartment', 'Office apartment']
- DAYS_BIRTH: 출생일
  - 데이터 수집 당시 (0)부터 역으로 셈, 즉, -1은 데이터 수집일 하루 전에 태어났음을 의미
- DAYS_EMPLOYED: 업무 시작일
  - 데이터 수집 당시 (0)부터 역으로 셈, 즉, -1은 데이터 수집일 하루 전부터 일을 시작함을 의미. 양수 값은 고용되지 않은 상태를 의미함
- FLAG_MOBIL: 핸드폰 소유 여부
- work_phone: 업무용 전화 소유 여부
- phone: 전화 소유 여부
- email: 이메일 소유 여부
- occyp_type: 직업 유형													
- family_size: 가족 규모
- begin_month: 신용카드 발급 월
  - 데이터 수집 당시 (0)부터 역으로 셈, 즉, -1은 데이터 수집일 한 달 전에 신용카드를 발급함을 의미
- credit: 사용자의 신용카드 대금 연체를 기준으로 한 신용도
  - 낮을 수록 높은 신용의 신용카드 사용자를 의미함



## Experiments
### 기준 baseline [Simple Baseline LGBM - LB 0.72728 - 최정명](https://dacon.io/competitions/official/235713/codeshare/2476?page=1&dtype=vote)
> 내가 실행해보니 기준도 `0.8086858121`으로 더 낮았다. 그러면 experiment1이 괜찮은 걸까...
1. experiment 1 - `0.8076415252`
   - EDA 2, 3 을 확인해보면 중복된 데이터가 있는 것을 확인해볼 수 있었다. 이를 같은 사람으로 보지 않고, 같은 피처를 가진 개별 데이터로 보고 이 같은 피처들이 가진 타겟값의 평균을 파겟값으로 하여 중복 데이터는 삭제하였다.
> 중복된 데이터를 다른 사람으로 본다면, 이렇게 한 개의 데이터로 합치는 것이 아니라 각각의 데이터로 그냥 학습해준다면 이 중복된 여러 데이터가 해당 값에 대해 스스로 가중치를 부여해준다고 볼 수 있을까?

### custom standard baseline - `0.7611898663220819`
> 데이콘 일일 제출 가능 횟수가 3회여서 제출 없이 진행하기 위해 실험을 위한 기준이 되는 간단한 baseline
- 결측치 'NAN' 으로 처리
- `index` drop
- onehot encoding categorical feature

1. `0.7611898663220819`
   - `FLAG_MOBIL` drop : train, test 모두에 한 가지 데이터 밖에 없음
> 성능 변화 X -> 일단 drop해도 될듯
2. `0.7611898663220819`
- Binary Categorical Feature 처리
  - `gender`, `car`, `reality`, `work_phone`, `phone`, `email`, `FLAG_MOBIL`(drop)
    - 이 중 object type: `gender`, `car`, `reality`
  - 기존의 baseline은 모두 onehotencoding 
  - 이외사항 1과 동일
> fit_time 만 줄어들었을 뿐 성능에서는 영향을 미치지 않았다. -> 일단 이렇게 진행하도록
3. `0.7629209081254806` - bad
   - 결측치가 많은 `occyp_type` drop
   - 이외 2와 동일

4. `family_size`, `child_num` 처리
   - outlier처리
   - drop
   - `family_size` - `child_num` feature 추가 -> 이후 실험에서는 해당 feature를 `parent`라 하겠음
   - PCA 를 통한 차원 축소 
   - `fc` outlier 제거
> `family_size`, `child_num` 에 대한 outlier 처리를 해준 후 `family_size` - `child_num` feature 를 포함해 총 3 feature를 차원축소 해준 것이 가장 성능이 좋았다. 아래 표에 값을 해당 피처의 최대값으로 지정하고 그 이상인 값은 이상치로 간주해 최대값으로 조정해주는 식으로 처리하였다. family_size가 child_num 보다 작은 경우가 있고 이 경우는 있기 어려운 경우라 생각해서 고려하지 않아도 될 것 같다.


**성능이 좋았던 것으로 나타난 10개**
|family_size|child_num|score|
|---|---|---
|3|4|-0.7600580763343784|
|4|4|-0.7600580763343784|
|5|4|-0.7600580763343784|
|6|4|-0.7600580763343784|
|6|2|-0.7601985900920513|
|4|1|-0.760361712706606|
|4|2|-0.7604649642691491|
|0|4|-0.7604711560721625|
|1|4|-0.7604711560721625|
|5|3|-0.7605177956886361|

5.  scaling - `0.7600575656819766`
- `income_total`이 특정 값에 쏠려있어서 로그를 취해본다.
- 정규화를 진행해본다.
- 나머지 내용은 4와 같음
> `income_total` 로그화 했을 때 성능 미미하게 향상. minmaxscaling 에 대해서는 다른 값에 대해서는 성능이 떨어지고 `income_total`에 대해서만 성능의 변동이 없었다. 나중에 어떻게 할지 결정해야될듯.

6. 
- `DAYS_EMPLOYED` ==  365243 -> 0 - bad
  - `0.7600575656819766` -> `0.7773064081582921`
> 성능이 떨어졌다.. 왜...?

7. `edu_type` 교육 수준별로 라벨링 - bad

8. `edu_type` credit에 따라 순차적으로 라벨링 - bad

### 추가로 진행해볼 것
- 남은 outlier 처리
  - `income_type`의 Student 7개 뿐
- 의문의 Encoding 관련



## 의문
- 범주형 데이터(edutype 등)를 OnehotEncoding 이 아니라 특정 기준(교육수준)에 따라 OrdinalEncoding 하는 것이 성능이 좋아질까?
  - 임의의 기준(교육수준)이 아니라 target값에 따라(신용 등급이 더 높은 것에 더 높은 수 부여) Encoding 하는 것이 좋지 않을까
  - target값에 따라 기준을 구할 때 EDA 6 번 참조

## 확인해본 공유코드

### EDA
1. [입문자의 투박한 EDA](https://dacon.io/competitions/official/235713/codeshare/2494?page=1&dtype=vote)
   - feature 별 target과 관계 확인
   - 데이터 타입 파악

2. [전처리, EDA하면서 발생한 의문점 공유드립니다.](https://dacon.io/competitions/official/235713/codeshare/2509?page=1&dtype=view)
   - 동일인물 있나?

3. [데이터 중복 이슈에 대한 데이터 분석 초보의 고찰](https://dacon.io/competitions/official/235713/codeshare/2522?page=1&dtype=view)
   - 위 코드와 같은 문제를 다룸
   - 동일 인물에 대한 시간에 따른 신용도 변화 추이로 해석

4. [EDA for starters(가르침이필요해)](https://dacon.io/competitions/official/235713/codeshare/2485?page=1&dtype=vote)
   -  `FLAG_MOBIL` 피처 train, test에서 모두 같은 값(1) 밖에 없으므로 무의미한 정보로 봐도 무방할 듯
   -  `income_total` 로그를 취하면 노말에 가까워짐
   -  기타 다른 피처와 타겟값 사이 관계

5. [데이터를 변환하고 이상치를 제거해보자 !!(함께하는우리)](https://dacon.io/competitions/official/235713/codeshare/2565?page=2&dtype=vote)
   - 상관관계 높은 데이터 drop (`child_num`, `family_size`)
     - 두 피처에 대한 이상치
   - `occyp_type`
     - `credit` 비율이 train 전체와 `occyp_type` 이 NaN의 비율이 비슷
     - NaN이라고 `DAYS_EMPLOYED` 값이 0 인 것은 아님. 즉, 직업이 없는 상태 아님

6. [EDA 과정 중 고민해 볼만한 부분들 공유드립니다 (4/12)](https://dacon.io/competitions/official/235713/codeshare/2514?page=2&dtype=recent)
   - 고용 상태 별 신용 비율
   - 기타 outlier

7. [중복 데이터/ 오류 데이터 관련해서 이야기를 꺼내봅니다.(하르딘)](https://dacon.io/competitions/official/235713/codeshare/2676#)

### pycaret
1. [Pycaret logloss baseline (LB 0.75267) Jay 윤](https://dacon.io/competitions/official/235713/codeshare/2477?page=1&dtype=vote)
   - `pycaret`에 대해 한번 사용해볼 겸 공유코드 따라가봄
   - 이외 공식문서를 통한 조금의 추가실습
