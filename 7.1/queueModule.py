#!/usr/bin/env python
# coding: utf-8

# 큐 배열  => 주로 스케줄링에 많이 쓰인다고 함  
# 입력은 뒤(rear, tail)  
# 출력은 앞(front, head)  

# In[24]:


class Queue :
    #  외부에서 데이터 배열의 사이즈를 얻어오는 생성자 만들기
    def __init__ (self, size=5): 
        self.size = size # 큐 배열의 크기
        self.rear = 0 # 데이터가 추가되면 증가
        self.front = 0 # 데이터를 출력하면 증가
        self.queue = list() # 데이터를 담아줄 연속 리스트 생서
        
    # 데이터 입력 받기
    def add(self, data):
        # 우선 중복 검사
        if data not in self.queue:
            # overflow 검사
            if self.rear < self.size: 
                # 오버플로우 아닐 때
                self.queue.append(data)
                self.rear += 1
            else : # 오버 플로우 일때
                print('overflow!!')
            # ==== if size
        else :
            print('{}는 중복된 data'.format(data))
        # === if not in
        self.view()
    # remove (삭제)
    def remove(self):
        # 저장된 데이터가 없을 때
        if self.rear < 0 or self.front == self.rear :
            print('underflow!')
        # === if front == rear
        else : 
            data = self.queue[self.front]
            self.queue[self.front] = '' # 공백처리해야 어색하지 않다
            self.front += 1
            print('{} 데이터 삭제'. format(data))
        self.view()
    
    def view(self):
        # 데이터 없을 때
        if self.rear < 0 or self.front == self.rear :
            print('don\'t have data')
        else : 
            print('queue ==> ',end = '')
            for i in range(self.front,self.rear):
                print(self.queue[i],end = ' ')
            print(',,,rear : {}, front : {}'.format(self.rear, self.front))
        # ===== if front == rear
                
        


# In[29]:


if __name__=='__main__':
    queue = Queue(6)
    queue.view()
    queue.add(2)
    queue.add(2)
    queue.add(4)    
    queue.add(6)    
    queue.add(8)    
    queue.add(10)    
    queue.add(12)    
    queue.add(14)    
    print('='*60)
    queue.remove()
    queue.remove()    
    queue.remove()    
    queue.remove()    
    queue.remove()    
    queue.remove()    
    print('='*60)
    queue.view()
    queue.add(4)
    

