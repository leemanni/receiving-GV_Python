#!/usr/bin/env python
# coding: utf-8

# In[1]:


# linkedList 에 저장할 데이터를 기억하는 클래스 => node
class Node :
    def __init__(self, data):
        self.data = data # 실제의 데이터
        self.next = None  # 다음 위치의 데이터주소


# In[68]:


# linkedList 자체를 저장하는 클래스 => 입력, 출력, 삭제 다 할 거임
class LinkedList :
    def __init__(self):
        self.head = None # 리스트의 시작위치
        self.count = 0 # 배열에 들어가 데이터의 수
        
        
        
    # 1. 데이터 입력
        # 1-1. 데이터 맨 뒤에 추가(아무 것도 없을 떄도 해당)
    def appendLast(self, data):
        newnode = Node(data) # 입력 받은 데이터를 객체화
        start = self.head # 시작 위치를 가독성을 위해 변수에 담는다
        self.count += 1 # 입력 받자마자 데이터 수 증가 시킨다

        if self.head is None : # 데이터가 들어 있는 지 여부
            # 비어 있음
            self.head = newnode # 아무 것도 없기 때문에 시작위치에 주소 넣음
            return # 들어가면 함수를 끝낸다
        # 뭔가 들어있는 경우
        while start.next : # 다음번에 없으면 무한반복 탈출
            start = start.next
        start.next = newnode # 맨 막지막에 데이터 추가
                
    # 1-2. 데이터 맨 처음에 추가
    def insertFirst(self,data):
        newnode = Node(data) # 받은 데이터 객체화
        self.count += 1 
        newnode.next = self.head
        self.head = newnode
            
    # 1-3. 중간에 추가
    def insertPosition(self, position, data):
        # 포지션 잘못 짚었을때
        if position < 1 or position > self.count-1 :
            print('잘못된 위치 입니다.')
            return
        newnode = Node(data)
        self.count += 1
        start = self.head
        for i in range(position-1):
            start = start.next
        newnode.next = start.next
        start.next = newnode
        
    # 2. 데이터를 출력하는 함수
    def listPrint(self):
        start =self.head
        if start : # 비어 있는지 여부 판단
            print('현재 {}개의 데이터 존재'.format(self.count))
            for i in range(self.count):
                print(start.data, end = ' ')
                start = start.next
            print()
        else:
            print('empty;;')
    # 3. 제거
    def remove(self, data):
        start = self.head
        if start : # 안에 뭔가 있을 때
            # 3-1 제거할 위치가 맨 앞인 경우
            if start.data == data :
                self.head = start.next
                self.count -= 1
                return
             # 3-2 아닌경우
            while start is not None : ## 마지막 까지 찾아라
                if start.data == data :
                    break
                prev = start
                start = start.next # 이것이 무한 루프 탈출의 키
            if start == None :
                print('{}는 저장소에 존재하지 않습니다'.format(data))
                return
            prev.next = start.next
            self.count -= 1
        else:
            print('empty;;')
            


# In[70]:


linkedList = LinkedList()
linkedList.appendLast('태연')
linkedList.listPrint()
linkedList.appendLast('운아')
linkedList.listPrint()
linkedList.insertFirst('티파니')
linkedList.listPrint()
linkedList.insertPosition(1,'서현')
linkedList.listPrint()

print('='* 40)
linkedList.remove('티파니')
linkedList.listPrint()
linkedList.remove('태연')
linkedList.listPrint()


