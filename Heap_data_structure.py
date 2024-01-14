#---------------Time Complexity-------------------------#
# To insert Singe element in Heap:    O(logn)
# To delete Single element from Heap: O(logn)
# Given array of element to heapify:  O(n)
# To build heap with n elements:      O(nlogn)




class Heap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)//2


    def leftChild(self,index):
        return 2*index+1


    def rightChild(self,index):
        return 2*index+2
    
    def _heapify_up(self,type):
        if type=="min":
            i=n=len(self.heap)-1
            while(i>0):
                if self.heap[i]<self.heap[(self.parent(i))]:
                    self.heap[i],self.heap[(self.parent(i))]=self.heap[(self.parent(i))],self.heap[i]
                    i=self.parent(i)
                else:
                    break

        if type=="max":
            i=n=len(self.heap)-1
            while(i>0):
                if self.heap[i]>self.heap[(self.parent(i))]:
                    self.heap[i],self.heap[(self.parent(i))]=self.heap[(self.parent(i))],self.heap[i]
                    i=self.parent(i)
                else:
                    break
            
            
            
    
    def heappush(self,data,type="min"):
        self.heap.append(data)
        if type=="max":
            self._heapify_up("max")
        else:
            self._heapify_up("min")
            
    def _heapify_down(self,type):
        index=0
        if type=="max":
            while True:
                max_index=index
                if self.leftChild(index)<len(self.heap) and self.heap[self.leftChild(index)]>self.heap[max_index]:
                    max_index=self.leftChild(index)
            
                if self.rightChild(index)<len(self.heap) and self.heap[self.rightChild(index)]>self.heap[max_index]:
                    max_index=self.rightChild(index)
            
                if max_index!=index:
                    self.heap[index],self.heap[max_index]=self.heap[max_index],self.heap[index]
                    index=max_index
                else:
                    break
        if type=="min":
            while True:
                min_index=index
                if self.leftChild(index)<len(self.heap) and self.heap[self.leftChild(index)]<self.heap[min_index]:
                    min_index=self.leftChild(index)
            
                if self.rightChild(index)<len(self.heap) and self.heap[self.rightChild(index)]<self.heap[min_index]:
                    min_index=self.rightChild(index)
            
                if min_index!=index:
                    self.heap[index],self.heap[min_index]=self.heap[min_index],self.heap[index]
                    index=min_index
                else:
                    break
                
            
            
    def heappop(self,type='min'):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        x=self.heap.pop()
        
        if type=='max':
            self._heapify_down("max")
        else:
            self._heapify_down("min")
        return x
    
    def heapsort(self,List=None)->list:
        pass
    
    # To heapify external list(to convert in min give type="min" otherwise="max")
    # By default it is min heap.
    def heapify(self,List=None,type='min')->list:
        if List:
            if type=='max':
                i=n=len(List)
                while(i>0):
                    j=i-1
                    while(j<n):
                        if self.leftChild(j)<len(List):
                            if self.rightChild(j)<len(List):
                                if List[self.leftChild(j)]>List[self.rightChild(j)] and List[j]<List[self.leftChild(j)]:
                                    List[j],List[self.leftChild(j)]=List[self.leftChild(j)],List[j]
                                    j=self.leftChild(j)
                                elif List[self.leftChild(j)]<List[self.rightChild(j)] and List[j]<List[self.rightChild(j)]:
                                    List[j],List[self.rightChild(j)]=List[self.rightChild(j)],List[j]
                                    j=self.rightChild(j)
                            else:
                                if List[j]<List[self.leftChild(j)]:
                                    List[j],List[self.leftChild(j)]=List[self.leftChild(j)],List[j]
                                    j=self.leftChild(j)
			
                        else:
                            break
                    i-=1


            if type=='min':
                i=n=len(List)
                while(i>0):
                    j=i-1
                    while(j<n):
                        if self.leftChild(j)<len(List):
                            if self.rightChild(j)<len(List):
                                if List[self.leftChild(j)]<List[self.rightChild(j)] and List[j]>List[self.leftChild(j)]:
                                    List[j],List[self.leftChild(j)]=List[self.leftChild(j)],List[j]
                                    j=self.leftChild(j)
                                elif List[self.leftChild(j)]>List[self.rightChild(j)] and List[j]<List[self.rightChild(j)]:
                                    List[j],List[self.rightChild(j)]=List[self.rightChild(j)],List[j]
                                    j=self.rightChild(j)
                            else:
                                if List[j]>List[self.leftChild(j)]:
                                    List[j],List[self.leftChild(j)]=List[self.leftChild(j)],List[j]
                                    j=self.leftChild(j)
			
                        else:
                            break
                    i-=1
        return List
                
                
                






#----------------Driver Function-------------------#


if __name__=="__main__":
    h=Heap()
    #print(h.heapify([1,2,4,6,7],type='max'))
    h.heappush(10,'max')
    h.heappush(11,'max')
    h.heappush(15,'max')
    h.heappush(12,'max')
    
    print(h.heap)
    print(h.heappop('max'))
    print(h.heappop('max'))
    print(h.heappop('max'))
    