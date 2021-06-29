#!/usr/bin/env python
# coding: utf-8

# In[33]:


while True :
    n = int(input('보고싶은 마방진 배열을 입력하세요(3이상 홀수) : '))
    if n % 2 ==1 and n >= 3 :
        break
    else :
        print('3이상이고 홀수만 입력하세요')
magicArray = [[0]*n for i in range(n)]
i = 0 # 행 
j = n // 2 # 

for p in range(1, n**2+1):
    magicArray[i][j] = p
    # 다음 수 가 차수의 배수일때
    if p % n == 0 : # 배수면 바로 아래에 채워준다(행 +1)
        i += 1
    # 배수가 아닝 때
    else : # 오른쪽 위 에 (행 -1, 열 +1)
        i -= 1
        
        j += 1
        if i < 0 :
            i = n-1 # 행의 마지막 위치
        elif j == n :
            j = 0
for i in  range(len(magicArray)):
    for j in range(len(magicArray[i])):
        print(' {:3d} '.format(magicArray[i][j]),end = '')
    print()

