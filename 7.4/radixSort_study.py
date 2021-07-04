#!/usr/bin/env python
# coding: utf-8

# In[5]:


data = list()
while True :
    n = int(input('정수를 입력하세요(중복된 수를 넣으면 프로그램 종료 ) : '))
    if n in data :
        break
    data.append(n)


# In[6]:


isSort =False
radix = 1
while not isSort :
    isSort = True
    queueList = [[]for i in range(10)]
    index = 0 # 큐 리스트에 저장된 데이터를 0번 부터 꺼내서 data에 정렬해주는 인덱스
    print('radix : {}'.format(radix))
    for k in data:
        print('{}==>'.format(k), end = '')
        digit = k // radix % 10 # 각 자리수와 그 자리수의 수 만큼의 인덱스 배열에 넣어주는 변수
        print(digit)
        queueList[digit].append(k)
        if isSort and digit > 0 :
            isSort = False
    for numbers in queueList : # 자리수 1~9 배열의 수를 분리해줌
        #  리스트 안에 데이터가 없으면 이 반복은 돌아가지 않고 나온다.
        for number in  numbers :
            data[index] = number
            index += 1
    print(data)
    print('='*100)
    radix *= 10

