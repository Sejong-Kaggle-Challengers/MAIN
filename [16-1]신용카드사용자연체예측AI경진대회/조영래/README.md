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
1. experiment 1

- EDA 2, 3 을 확인해보면 중복된 데이터가 있는 것을 확인해볼 수 있었다. 이를 같은 사람으로 보지 않고, 같은 피처를 가진 개별 데이터로 보고 이 같은 피처들이 가진 타겟값의 평균을 파겟값으로 하여 중복 데이터는 삭제하였다.
- 이외 과정은 [Simple Baseline LGBM - LB 0.72728 - 최정명](https://dacon.io/competitions/official/235713/codeshare/2476?page=1&dtype=vote) 과 같다.
- 성능 `0.8076415252` 로 저하되었다.


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
   - `occyp_type`
     - `credit` 비율이 train 전체와 `occyp_type` 이 NaN의 비율이 비슷
     - NaN이라고 `DAYS_EMPLOYED` 값이 0 인 것은 아님. 즉, 직업이 없는 상태 아님

### pycaret
1. [Pycaret logloss baseline (LB 0.75267) Jay 윤](https://dacon.io/competitions/official/235713/codeshare/2477?page=1&dtype=vote)
   - `pycaret`에 대해 한번 사용해볼 겸 공유코드 따라가봄
   - 이외 공식문서를 통한 조금의 추가실습