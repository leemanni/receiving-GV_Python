#!/usr/bin/env python
# coding: utf-8

# <게시판 페이징>  
# 입력 ==> 총 건수(m) , 한 페이지에 보여줄 게시물 수(n)  
# (단, n은 1보다 크거나 같다. n>=1)  
# 게시물의 총 건수와한 페이지에 보여줄 게시물 수를 입력했을 때  
# 총 페이지 수를 리턴하는 프로그램  

# In[26]:


def tablePaging( m , n ):
    if n < 1 :
        return '한 페이지에 보여줄 게시물 수는 1 이상이어야 한다.'
    page = m // n  + 1 if m % n > 0 else m // n
    return '총 페이지 수 : {}'.format(page)


# In[27]:


tablePaging(0, 1)


# In[33]:


tablePaging(41,3)

