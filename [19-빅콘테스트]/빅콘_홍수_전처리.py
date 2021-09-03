#!/usr/bin/env python
# coding: utf-8

# In[19]:


#이상치 제거

def outlier_iqr(data):
  q1, q3 = np.percentile(data, [25, 75])
  iqr = q3-q1
  lower = q1- (iqr*1.5)
  upper = q3 + (iqr*1.5)

  return np.where((data > upper) | (data < lower))


# In[ ]:


outlier_1 = outlier_iqr(train.loc[train['홍수사상번호']==1].유입량)[0]
outlier_12 = outlier_iqr(train.loc[train['홍수사상번호']==12].유입량)[0]
outlier_15 = outlier_iqr(train.loc[train['홍수사상번호']==15].유입량)[0]
outlier_16 = outlier_iqr(train.loc[train['홍수사상번호']==16].유입량)[0]
outlier_20 = outlier_iqr(train.loc[train['홍수사상번호']==20].유입량)[0]
outlier_22 = outlier_iqr(train.loc[train['홍수사상번호']==22].유입량)[0]


# In[ ]:


outlier_index = np.concatenate([outlier_1, outlier_12, outlier_15, outlier_16, outlier_20, outlier_22], axis=0)

outlier_index = set(outlier_index)

for i in outlier_index:
  train = train.drop(index=i, axis = 0)


# In[ ]:


#시간데이터 삭제

train = train.drop(['연', '월', '일', '시간'], axis=1)

