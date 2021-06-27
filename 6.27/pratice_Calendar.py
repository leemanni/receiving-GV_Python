#!/usr/bin/env python
# coding: utf-8

# 시험공부 : 달력만들기 ~  
# 1. 윤년 평년 판독 함수  
# 2. 년과 월을 입력하면 마지막 날을 알려주는 함수  
# 3. 1년 1월 1일 부터 지금까지의 날짜 수를 구해주는 함수  
# 4. 오늘이 무슨 요일인지 숫자로 알려주는 함수(ex : 일요일(0), 월요일(1).....금요일(5),토요일(6))  
# 5. 위의 4개를 조합해서 달력을 만들기

# In[9]:


# 1 윤년 & 평년을 알려주는 함수
def isLeapYear(year) :
    return True if year % 4 ==0 and year % 100 !=  0 or year % 400 ==0 else False


# In[11]:


# 2 년과 월을 입력하면 마지막 날을 알려주는 함수
def lastDay(year, month):
    m =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) :
        m[1] = 29
    return m[month-1]


# In[15]:


# 3 1년 1월 1일 부터 지금까지 날짜 수를 구해주는 함수
def totalDay(year, month, day) :
    y = year -1 
    total = y * 365 + y // 4 - y // 100 + y // 400
    for i in range(1,month):
        total += lastDay(year,i)
    return total + day


# In[17]:


#4 오늘이 무슨 요일인지 숫자로 알려주는 함수
def weekDay(year, month, day):
    return totalDay(year,month,day) % 7


# In[40]:


# 5 위의 함수들을 이용해서 달력만들기
year, month = map(int,input('보고싶은 년과 달을 입력하세요 :').split())
print('='*30)
print('          {:4d}년{:02d}월'.format(year,month))
print('='*30)
print(' 일  월  화  수  목  금  토')
print('='*30)
for i in range(weekDay(year, month, 1)) :
    print('    ',end = '')
for i in range(1,lastDay(year, month)+1):
    print(' {:2d} '.format(i),end = '')
    if weekDay(year, month, i) == 6 and lastDay(year,month) != i:
        print()
print('\n'+'='*30)


# In[ ]:




