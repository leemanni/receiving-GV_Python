#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1
# 연을 입력받아서 윤년인지 평년인지 판단하는 함수
def isLeapYear(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 ==0 else False


# In[93]:


# 2 
# 매개변수(인수)로 년 월을 입력받아서 해당 달의 마지막 날을 입력받는 함수
def lastDay(year , month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    if isLeapYear(year) :
        m[1] = 29
    return m[month-1]


# In[86]:


# 3
# 년, 월, 일을 입력받아 1년 1월 1일 부터 지금까지의 날을 보여주는 함수
def totalDay(year, month, day):
    # 작년까지의 모든 날을 더해준다.
    total = 365 * (year-1) + (year-1) // 4  - (year-1) // 100 + (year-1) // 400
        # 윤년인 날을 추가하기 위해 생각해보자 
        # 4로 나눠떨어지고 & 100으로 나눠 떨어지지 않거나 | 400으로 나눠떨어지는것
        # 윤년인 날을 구해보자면 이 조건대로 나눠떨어지는 날은 더해주고 나눠 떨어지지 않는 날은
        # 빼주면 윤년이엇던 해의 총 개수 즉, 1년이 366일 이었던 날을 구해서 더해줄 수 있다.
    # 직전 월까지의 날을 더해준다.
    for i in range(1, month):
        total += lastDay(year, i)
    return total + day # 일수는 그냥 더해줘도 상관 없음.


# In[111]:


#  지금까지의 날을 기준으로 요일을 구해주는 함수(일요일 : 0...토요일 : 6)
def weekDay(year,month,day):
    return totalDay(year, month, day) % 7


# In[112]:


print(weekDay(2021, 6, 24))


# In[164]:


# 5 달력을 만들어보기
year, month =map(int,input('보고싶은 년도의 월을 입력하세요 : ').split())
print('='* 28)
print('       {}년{}월'.format(year,month))
print('='* 28)
print(' 일  월  화  수  목  금  토')
print('='* 28)
for i in range(weekDay(year,month,1)) :
    print('    ',end ='')
for i in range(1, lastDay(year,month)+1):
    print(' {:2d} '.format(i),end = '')
#     k = weekDay(year,month)
    if weekDay(year,month,i) ==6  and i != lastDay(year,month) :
        print()
print('\n','='* 28)

