#!/usr/bin/env python
# coding: utf-8

# 문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를  
# 구해서 표시하고, 문자열을 압축하기  
# 입력예시 : aaabbcccccca  
# 출력예시 : a3b2c6a1  

# In[51]:


def runLength(text) :
    returnList = list() # 새롭게 리턴하는 리스트
    cnt = 1 # 연속으로 같은 문자인지 확인하는 변수
    for i in range(1,len(text)):
        if text[i-1] == text[i] :
            cnt += 1
        else :
            returnList.append(text[text.index(text[i-1])])
            returnList.append(cnt)
            cnt = 1
    returnList.append(text[-1])
    returnList.append(cnt)
    for i in range(len(returnList)):
        print(returnList[i],end='')


# In[52]:


runLength('aaabbccccccaa')


# In[59]:


def runLength(text) :
    returnString = text[0] 
    cnt = 0 # 연속으로 같은 문자인지 확인하는 변수
    for i in text:
        if i == returnString[-1] :
            cnt += 1
        else :
            returnString += str(cnt) + i
            cnt = 1
    returnString += str(cnt)
    print(returnString)


# In[60]:


runLength('aaabbccccccaa')

