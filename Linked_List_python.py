class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class Linked_List:
    def __init__(self,data):
        self.head=Node(data)
        
    # Inserting Node at beginning of Linked List.
    def InsertNode_atBeg(self,data):
        if self.head:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
    
    # Printing Linked List.
    def print_LL(self):
        if self.head:
            temp=self.head
            while(temp!=None):
                print(temp.data,end=' ')
                temp=temp.next
            print()
        else:
            print("Linked List is empty: Nothing to print.")
    
    # Inserting Node at end of Linked List.
    def InsertNode_atLast(self,data):
        temp=self.head
        while(temp.next!=None):
            new_node=Node(data)
            temp=temp.next
        temp.next=new_node
        
    # Reversing Linked_List.
    
    def Reverse_LL(self):
        p1=self.head
        p2=self.head.next
        self.head.next=None
        while(p2!=None):
            temp=p2.next
            p2.next =p1
            p1=p2
            p2=temp
        self.head=p1
    def Remove_LastNode(self):
        
        if self.head==None:
            print("Linked List is Empty: Nothing to delete.")
        
        else:
            if self.head.next==None:
                self.head=None
            
            else:
                temp=self.head
                while(temp.next.next!=None):
                    prev=temp
                    temp=temp.next
                temp.next=None
    
    
    def Remove_FirstNode(self):
        if self.head:
            self.head=self.head.next
        else:
            print("Linked List is empty: Nothing to delete.")
        

# driver function

if __name__=='__main__':
    LL=Linked_List(5)
    # calling function to insert Node at beginning.
    LL.InsertNode_atBeg(4)
    LL.InsertNode_atBeg(5)
    LL.InsertNode_atBeg(6)
    LL.InsertNode_atBeg(7)
    
    # printing Linked List.
    LL.print_LL()
    
    # calling function to insert Node at end.
    LL.InsertNode_atLast(11)
    LL.InsertNode_atLast(12)
    LL.InsertNode_atLast(13)
    LL.print_LL()
    # Reversing Linked List.
    LL.Reverse_LL()
    LL.print_LL()
    LL.Remove_LastNode()
    LL.Remove_LastNode()
    LL.Remove_LastNode()
    LL.Remove_FirstNode()
    LL.Remove_LastNode()
    LL.Remove_FirstNode()
    LL.print_LL()
    LL.Remove_FirstNode()
    LL.print_LL()
    LL.Remove_LastNode()
    LL.print_LL()
    LL.Remove_LastNode()
    LL.Remove_FirstNode()
    
    