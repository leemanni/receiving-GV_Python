#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 
#그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 
#이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 
#예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라


# In[32]:


def gener(number):
    n = number
    for i in str(number):
        n += int(i)
    return n
numbers = set(range(1,5001))
generator = set(gener(i) for i in range(1,5001))
sum(numbers - generator)

