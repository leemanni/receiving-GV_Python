#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Stack :
    # constructor
    def __init__(self, size = 5) :
        self.size = size
        self.stack = list()
        self.top = 0
        
    # push
    def push(self, data):
        if data not in self.stack :
            if self.size > self.top:
                self.stack.append(data)
                print('데이터 저장 완료')
                self.top += 1
            else:
                print('overflow')
        else :
            print('중복!...{} 데이터는 받을 수 없습니다'.format(data))
        self.view()
        
    #pop
    def pop(self):
        if self.top == 0 :
            print('제거할 데이터 없음')
        else :
            data = self.stack.pop()
            self.top -= 1
            
            # pop() 은 제거할 데이터를 가지고 있다가 없애는 것을 이용
            print('{} 가 제거되었습니다'.format(data))
            self.view()
            
    #view
    def view(self) :
        if self.top != 0 :
            print('stack==> ',end ='')
            for i in range(self.top):
                print(self.stack[i],end=' ')
        else : # 데이터가 없을 때
                print('underflow!! 데이터가 없어용')
        print()
            
            


# In[34]:


if __name__ == '__main__' :
    st = Stack()
    st.push(25)
    st.push(34)
    st.push(33)
    st.push(34)
    st.push(1)
    st.push(2)
    st.push(33)
    print('='*35)
    st.pop()
    st.pop()
    st.pop()
    st.pop()
    st.pop()
    st.pop()

