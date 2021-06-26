#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 각 점수별로 별을 넣어주는 함수
def instar (listA) :
    star = list()
    for i in range(listA//10) :
        star.append('★')
    if listA % 10  >= 5 and len(star) !=10 :
        star.append('☆')
    for i in range(10 - len(star)):
        star.append('   ')
    return star


# In[2]:


# 데이터 입력받기
n = 0 
data =list()
while n != 999 :
    n = int(input('점수를 입력하세요 : '))
    data.append(n)
data.pop()
print(data)


# In[5]:


# 입렫받은 데이터를 dict() 에 담아두기
outstar = dict()
for i in  range(len(data)):
    for j in range(len(data)):
        outstar[data[i]] = instar(data[i])
# print(outstar)


# In[8]:


for i in range(len(instar(data[0]))-1,-1,-1):
    print(' {:3d} │ '.format((i+1)*10),end='')
    for j in range(len(data)) :
        print(' {:2s} '.format(outstar.get(data[j])[i]),end='')
    print()
print('      '+'───'* len(data)) # 6번 공백
print('       ',end='')
for i in range(len(data)):
    print(' {:3d} '.format(data[i]),end='')

