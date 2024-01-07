import heapq

#---------------------- min Heap------------------------------#

min_heap=[]

# push element into the min heap

heapq.heappush(min_heap,10)
heapq.heappush(min_heap,11)
heapq.heappush(min_heap,4)
heapq.heappush(min_heap,5)
heapq.heappush(min_heap,6)


# printing min_heap list.
print('printing min heap: ',min_heap) #[4,5,10,11,6]

# popping element from min heap
print("1st min element: ",heapq.heappop(min_heap)) # 4
print("2nd min element: ",heapq.heappop(min_heap)) # 5



#---------------------- max Heap------------------------------#

# Note: min heap is by default inbuilt data structure in python.
#    To perform max heap insert negative element and pop negative of same.
max_heap=[]
heapq.heappush(max_heap,-10)
heapq.heappush(max_heap,-11)
heapq.heappush(max_heap,-4)
heapq.heappush(max_heap,-5)
heapq.heappush(max_heap,-6)

# printing max heap
print("printing max_heap: ",max_heap)


# popping elements from max heap:
print("1st max element: ",-heapq.heappop(max_heap)) # 11
print("2nd max element: ",-heapq.heappop(max_heap)) # 10


# heapify given list:
h=[10,11,4,5,6]
print("list before heapify: ", h)
heapq.heapify(h)
print("list after heapify: ", h)

# other heap method:
# 1. heapq.nlargest(n,h)  --> return n largest element.
# 2. heapq.nsmallest(n,h) --> return n smallest element.

# 3. heappushpop(heap,item) -->push and then it will pop smallest element.
# 4. heapreplace(heap,item) -->pop smallest element ,then insert element.(make sure heap is not empty.)
