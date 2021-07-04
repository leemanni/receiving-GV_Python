#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image
Image ('../workspace/photo/money_1.png',width=1000)


# In[2]:


Image ('../workspace/photo/money_2.png',width=1000)


# In[3]:


Image ('../workspace/photo/money_3.png',width=1000)


# In[30]:


class Money : 
    def __init__(self, name, money):
        self.name = name  # 이름을 받아두는 변수
        self.money = money # 금액을 받아두는 변수
        self.pm = [0  for i in range(10)] # 개인별 화폐별 개수를 저장하는 리스트
        # 이제 아래에 선언되는 변수는 생성자 안에서만 사용할 변수들이라 지역변수로 선언하였음
        m = 50000 # 화폐를 저장해주는 변수(초기값 50000원)
        sw = 1 # 화폐 변경의 방향을 알려주는 변수
        t = money
        
        for i in range(10):
            self.pm[i] = t // m
            t %= m
            if sw ==1 :
                m //= 5 ; sw = 0
            else :
                m //= 2 ; sw = 1
            # == sw == 0
        # === for k in range(10)
        
    def __str__(self):
        return '{:} : {:5,d}원==> {:}'.format(self.name, self.money, self.pm)


# In[36]:


creditor = [] # 객체들을 저장할 리스트
while True:
    name = input('이름을 입력하세요 : ')
    if name.lower() == 'quit' :
        break
    money = int(input('금액을 입력세요'))
    m = Money(name, money)
    creditor.append(m)


# In[117]:


tm = [0 for i in range(10)]
total = 0
print('                                          [직원별 출장수당 표]')
print('='*110)
print('  이름        금액      50,000   10,000   5,000   1,000    500    100     50      10       5       1')
print('='*110)
for i in creditor:
    print(' {:3s}     {:8,d} '.format(i.name, i.money),end='')
    total += i.money
    for k in range(len(i.pm)):
        print('     {:2d} '.format(i.pm[k]), end='')
        tm[k] += i.pm[k]
    print()
print('='*110)
print('  합계     {:7,d}      '.format(total),end = '')
for i in range(len(tm)):
    print('{:2d}      '.format(tm[i]),end = '')
print()
print('='*110)


