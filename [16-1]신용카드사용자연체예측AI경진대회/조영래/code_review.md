## [[Private 1위 0.6581] | 소회의실 | Catboost](https://dacon.io/competitions/official/235713/codeshare/2768?page=1&dtype=recent)
- catboost 이용 -> parameter tuning 하지 않았다...
- ID feature 생성 -> catboost로 학습했을 때 feature importance가 가장 높게 나왔다고 한다...
- 범주형 데이터를 Onehot encoding 이 아니라 Ordinal encoding으로 처리
  - catboost가 sparse한 데이터에 좋지 않다고 하였는데 그래서 Ordinal로 처리한건가..
- 클러스터링

## [[Private 2위 0.65862] | dswook | Stacking Ensemble](https://dacon.io/competitions/official/235713/codeshare/2757?page=1&dtype=recent)
- catboost
- categorical feature를 많이 만들으려 함
- optuna를 이용한 parameter tuning