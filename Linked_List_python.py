class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linked_List:
    def __init__(self,data):
        self.head=Node(data)
    
    def createNode(self,data):
        pass
    def InsertNode_at_beg(self,data):
        if self.head:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
    def print_LL(self):
        while(self.head!=None):
            print(self.head.data,end=' ')
            self.head=self.head.next
        
# driver function

if __name__=='__main__':
    LL=Linked_List(5)
    LL.InsertNode_at_beg(4)
    LL.InsertNode_at_beg(5)
    LL.InsertNode_at_beg(6)
    LL.InsertNode_at_beg(7)
    LL.print_LL()

    