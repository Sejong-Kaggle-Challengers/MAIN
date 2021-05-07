1. 전처리

flag_mobil,index 제거 : 유지
중복제거 : 제거 안하는게 성능 좋다.
DAYS_BIRTH,DAYS_EMPLOYED 음수 -> 양수 : 하는게 보통 성능 향상 확인. (본인은 제거)
family_size : 20,15 제거 이상치라 판단.
occyp_type : 결측값 채우기
family#begin : family와 begin_month 합쳐서 진행. 성능 더 낮아진다. ordinal 인코딩 때문인지?
다중공선성 : child_num은 family와 DAYS_BIRTH는 여러 변수들과. 제거 했더니 성능 다운.

범주형은 get_dummy로 원핫인코딩
정규화는 열에대해서만. batch아니다. 

2. 모델링

홀드아웃 기법 test size 0.15 seed 고정.
종속변수 불규칙하니 계층적으로 나누기.
xgb 사용. multi:softprob로 epoch 많이 돌리고 early_stop으로 멈추기.
metric은 logloss로






