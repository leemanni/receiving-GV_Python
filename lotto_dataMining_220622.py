#!/usr/bin/env python
# coding: utf-8

# 로또 출력하고 매 번 나온 숫자들의 횟수 데이터를 수집해보기

# In[24]:


import random
lotto = [i for i in range(1,46)] # 추첨하는 로또
dataLotto = [i for i in range(1,46)] # 1~45 까지 담긴 저장공간


# In[83]:


cnyLotto = [0 for i in range(1,46)] # 1~45 까지 나온 횟수 데이터를 담는 저장공간
for i in range(0,1000):
    random.shuffle(lotto) # 로또 번호 출력을 위한 출력
    
    # 로또 번호 1~7 번 째 숫자랑 같은 원본 인덱스 착아서 카우트 ++
    for k in range(7):
        cnyLotto[dataLotto.index(lotto[k])] +=1
# 데이터 추출
for i in range(len(cnyLotto)) :
    print('{}번 추첨된 횟수 : {} 회'.format(i+1,cnyLotto[i]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




