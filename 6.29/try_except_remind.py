#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 예외 처리를 이용해서 숫자와 문자가 혼용되어 있는 배열을 정렬하기
integer =list()
string = list()
while True :
    data = input('입력하세요(quit를 입력하면 프로그램 종료) :')
    if data.lower() =='quit':
        break
    try : # 우선 데이터를 정수화 해서 정수 리스트에 담는다
        integer.append(int(data))
    except : # 오류가 나면 해당 데이터를 문자열 리스트에 담는다.
        string.append(data)
integer.sort() ; string.sort()
print(integer + string)
    

