#!/usr/bin/env python
# coding: utf-8

# In[31]:


from module.calendarModule.makeCalendar_Module import *


# In[65]:


# 달력을 만들어 보기
def showCalendar() :
    year, month = map(int, input('보고싶은 년과 달을 입력하세요 :').split())
    print('=' * 30)
    print('         {:4d}년 {:02d}월'.format(year, month)) # 9 번 공백
    print('=' * 30)
    print(' 일  월  화  수  목  금  토') # 두번씩 공백 후 요일
    # 일수를 출력하기
    for i in range(weekDay(year, month, 1)):
        print('    ',end = '') # 공백 4번
    for i in range(1, lastDay(year, month+1)) :
        print(' {:2d} '.format(i),end='')
        if weekDay(year, month, i)  ==  6 and lastDay(year,month) != i:
            print()
    print('\n'+'=' * 30)


# In[68]:


showCalendar()

