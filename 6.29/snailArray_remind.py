#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [[0]*5 for i in range(5)]
n = 0 # 배열에 담아두는 변수
s = 1 # 배열 진행의 방향을 알려주는 변수
i = 0 # 행의 위치
j = -1 # 열의 위치 
k = 5 # 반복의 횟수를 알려줌
while True:
    for p in range(0,k):
        n += 1
        j += s
        a[i][j] = n
    k -= 1
    if k <= 0:
        break
    for p in  range(0,k):
        n += 1
        i += s
        a[i][j] = n
    s *= -1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(' {:3d} '.format(a[i][j]), end = '')
    print()


# In[27]:


a = [[0]*5 for i in range(5)]
n = 1 # 배열에 담아두는 변수
s = 1 # 배열 진행의 방향을 알려주는 변수
i = 2 # 행의 위치
j = 2 # 열의 위치 
k = 0 # 반복의 횟수를 알려줌
a[2][2] = 1
flag =False
while True:
    k += 1
    for p in range(0,k):
        n += 1
        j += s
        if n > 25 :
            flag = True
            break
        a[i][j] = n
    if flag :
        break
    for p in  range(0,k):
        n += 1
        i += s
        a[i][j] = n
#     k += 1
    s *= -1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(' {:3d} '.format(a[i][j]), end = '')
    print()

