#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 각 점수별로 별을 넣어주는 친구
def instar (listA) :
    star = list()
    for i in range(listA//10) :
        star.append('★')
    if listA % 10  >= 5 and len(star) !=10 :
        star.append('☆')
    for i in range(10 - len(star)):
        star.append('   ')
    return star


# In[ ]:


# 돌아가면서 별을 넣어주기
outStar = list()
data = [75, 94, 89, 95, 62]
temp = 10 - len(data)
for i in range(10-len(data),10) :
    data.append(0)
for i in range(len(data)) :
    outStar.append(instar(data[i]))
print(outStar)
# 다 역순으로 바꿔줘야함
for i in range(len(outStar)) :
    outStar[i].reverse()
print(outStar)


# In[ ]:


# 세로 막대 그래프 출력
for i in range(10): # 이친구도 10번 반복
    print('{:4d} │  '.format((10-i)*10),end = '') # 2번 공벡
    for j in range(10):
        print(' {:2s} '.format(outStar[j][i]),end='')
    print()
# print('     │',end='') # 5번 공백
print('      '+'─' * 20) # 6번 공백
print('         ',end='') # 4번 공백({:4d}) + 5번 공백
for i in range(len(data)-temp):
    print(' {:2d}  '.format(data[i]),end = '')

