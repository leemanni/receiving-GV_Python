#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 윤년 평년을 계산해주는 함수
def isLeapYear(year) : # True or False
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False


# In[2]:


# 2 달의 마지막 날을 리턴해주는 함수
def lastDay(year, month) : # 윤년 평년인지 판단해주기 위해서 year을 인수를 추가로 받아줘야함
    mDay = [31,28,31,30,31,30,31,31,30,31,39,31]
    if isLeapYear(year): # 윤년이니?
        mDay[1] = 29 # 윤년 이면 29일로 변경
    return mDay[month-1]


# In[4]:


# 3 '1년 1월 1일' 부터 지금 까지의 며칠인지 알려주는 함수
def totalDay(year, month, day):
    if year == 1 and month == 1 and day == 1 :
        total = 0 
    else :
        # 1 작년까지의 모든 날을 더해줌 year * 365 에 지금까지 윤년이었던 날을 구해주면 돼
        y = year -1 # 작년을 담아주는 변수
        total = 365 * y + y // 400 - y // 100 + y // 4
        # 1월 부터 전달까지 담아줌
        for i in range(1, month) :
            total += lastDay(year, i)
        total += day
    return total


# In[5]:


def weekDay(year , month, day) :
    return totalDay(year, month, day) % 7

