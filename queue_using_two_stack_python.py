# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:
    def __init__(self, size=50):
        self.stack=[]
        self.size=size
        self.top=-1
    
    def push(self, x):
        self.stack.append(x)
        self.top+=1
        
    def pop(self):
        if self.top!=-1:
            self.top-=1
            return self.stack.pop()

def enqueue(s1, s2, data):
    s1.push(data)
def dequeue(s1, s2):
    if s2.top==-1:
        if s1.top!=-1:
            while (s1.top!=-1):
                s2.push(s1.pop())
            s2.pop()
        else:
            return "Queue is Empty"
    else:
        s2.pop()

            
    

def print_front(s1, s2):
    if s2.top!=-1:
        print(s2.stack[s2.top])
    else:
        if s1.top!=-1:
            print(s1.stack[0])
        else:
            print("Queue is Empty.")
        
    
if __name__=='__main__':
    
    
    s1=Stack()
    s2=Stack()


n=int(input("How many operation you want to perform: "))
print("Note: for enqueue operation enter: 1 data.\n      for dequeue operation enter 2.\n      for print front element enter 3.")
for i in range(n):
    k=list(map(int, input().split()))
    if k[0]==1:
        enqueue(s1, s2,k[1])
    elif k[0]==2:
        dequeue(s1,s2)
    else:
        print_front(s1,s2)
