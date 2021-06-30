#!/usr/bin/env python
# coding: utf-8

# python 언어로 class를 이해해보기

# In[27]:


# 클래스를 선언해보기 => 3 과목 점수를 입력받고 합계와 평균을 게산하는 class
class Score :
    # 생성자 정의하기
    def __init__(self,name,age,python,java,c):
        self.name = name
        self.age = age
        self.python= python
        self.java = java
        self.c= c
    def totalSum(self) :
        self.total = self.java + self.python + self.c
        print('{}학생 총점 : {} 점'.format(self.name,self.total))
    def mean(self) :
        self.mean =  self.total / 3
        print('{}학생 평균 : {:.2f} 점'.format(self.name,self.mean))
    


# In[28]:


# 객체화 하기
sc1 = Score('이원희', 28, 85, 100, 89)
sc1.totalSum()
sc1.mean()


# In[ ]:





# In[ ]:





# In[ ]:




