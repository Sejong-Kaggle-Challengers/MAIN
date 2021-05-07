# [신용카드 사용자 연체 예측 AI 경진대회](https://dacon.io/competitions/official/235713/overview/description)

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
  