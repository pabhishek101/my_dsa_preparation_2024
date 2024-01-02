# Stack implementation in python (using python List.)

class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self)->bool:
        return len(self.items)==0
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is Empty."
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty."
    
    def size(self)->int:
        return len(self.items)



#---------------------Driver Function---------------------#

if __name__=='__main__':
    stack=Stack()
    print('Checking stack is empty ? : ',stack.is_empty())
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.push(15)
    print('Stack Size:',stack.size())
    print('Top element: ',stack.peek())
    print('pop: ',stack.pop())
    print('Stack Size:',stack.size())