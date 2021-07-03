#!/usr/bin/env python
# coding: utf-8

# In[39]:


class BinaryTree :
    # 1 생성자 만들기
    def __init__(self, data= None):
        self.left = None # 좌측 자식 노드의 위치
        self.data = data # 현재 노드의 데이터
        self.right = None # 우측 자식 노드의 위치
        
    # 2 데이터 삽입 
    def insert(self, data):
        print('현재 데이터 ==> {}'.format(data))

        # 좌측 노드로 갈 때(자식노드 < 루트 )
        if data < self.data :
            # 좌측에 데이터가 들어있는지 판단
            if self.left is None:
                # 데이터가 없는 경우
                self.left = BinaryTree(data)
                print('{} 좌측 노드에 {} 삽입 완료'.format(self.data,data))
                
            else :
            # 데이터가 들어있는 경우
                # 들어있으면 왼쪽 자식 노드의 왼쪽에 넣어야지
                print('{} 의 좌측으로 이동'.format(self.data))
                print('{} 에 도착'.format(self.left.data))
                self.left.insert(data) # 여기서 self.left 는 왼쪽 자식의 객체 즉(self.left.data)
                #  이것이 바로 재귀 함수의 활용
            # === if slef.left is None
        # ==== data < self.data
        
        # 우측 노드로 갈 때(자식노드 > 루트)
        elif data > self.data :
            # 똑같이 
            # 우측에 데이터가 있는지 판단.
            if self.right is None :
                # 데이터가 없는 경우
                self.right = BinaryTree(data)
                print('{} 의 우측 노드에 {} 삽입완료'.format(self.data,data))
            else :
                # 데이터가 있는 경우
                print('{} 의 우측으로 이동'.format(self.data))
                print('{} 에 도착'.format(self.right.data))
                self.right.insert(data) 
                # 이 재귀함수 기법은 우측 노드에 데이터가 없을 때까지 본인을 불러올 것이다.
            # == self.right is None
        # ==== data > self.data
        
        # 데이터가 중복일 경우
        else : 
            print('{}==>중복된 데이터이거나,  입력할 수 없는 값 입니다.'.format(data))
            
    # 3 데이터 탐색
    # 3-1 inorder
    def inorder(self): # 좌 -> 루트 -> 우
        if self.left :
            self.left.inorder() # 선택된 객체부터 좌측 노드에 값이 없을 때 까지 재귀함수 기법 발동
        # === left in None
        # == ask Last
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder()
    
    # 3-2 preorder : 루트 => 좌 => 우
    def preorder(self):
        print(self.data, end = ' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    # 3-3 postorder : 좌 => 우 => 루트
    def postorder(self) :
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end = ' ')
        
            
        
                
                
                
            
        


# In[ ]:





# In[40]:


binaryTree = BinaryTree(15)
print('='*75)
binaryTree.insert(8)
print('='*75)
binaryTree.insert(23)
print('='*75)
binaryTree.insert(12)
print('='*75)
binaryTree.insert(7)
print('='*75)
binaryTree.insert(18)
print('='*75)
binaryTree.insert(26)
print('='*75)


# In[41]:


binaryTree.postorder()


# In[34]:


binaryTree.inorder()


# In[35]:


binaryTree.preorder()

