#--------------sorting algo in python---------------#

# 1. Bubble sort
# 2. Selection sort
# 3. Insertion sort
# 4. Merge sort
# 5. Quick sort
# 6. Heap sort
# 7. Shell sort
# 8. Tree sort
# 9. Counting sort
# 10. Bucket sort
# 11. Radix sort
# 12. Topological sort


# 1 Bubble sort

#-------------------------------Key Analysis-----------------------------#

# time complexity:{ no of swap [n(n-1)/2)] + no of comparisons[n(n-1)/2)] }

#               (Worst case): O(n**2)        -- list is sorted in descending order.
#               (Best case) : O(n)           -- list is already sorted.
#               (Avg case)  : O(n**2)

# space complexity:
#               (worst case): O(1)

# Stable Algorithms: Yes
# Adaptive: Yes (after applying Flag)

#       Note:
#           1. In Nth pass we get Nth largest element in sorted position.
#           2. No of pass requires n-1.
#           3. 

#-------------------------------Bubble Sort Code Start-----------------------------#

def Bubble_sort(arr:list)->list:
    n=len(arr)
    for _ in range(n-1):
        swap=0
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                swap=1
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if swap==0:
            return
    return arr

#-------------------------------Bubble Sort Code End-----------------------------#




# 2. Selection sort

#-------------------------------Key Analysis-----------------------------#

# time complexity:{ no of swap (n-1) + no of comparisons[n(n-1)/2)]}

#               (Worst case): O(n**2)     
#               (Best case) : O(n**2)           
#               (Avg case)  : O(n**2)

# space complexity:
#               (worst case): O(1)

# Stable Algorithms: No
# Adaptive : No

#       Note:
#           1. Inplace sort Algorithms(no extra space required).
#           2. it requires min swapping.
#           3. In Kth pass we will get Kth shortest element.
#           4. No of pass requires n-1.

#-------------------------------Selection Sort Code Start-----------------------------#

def Selection_sort(arr:list)->list:
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        
        # swapping
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    return arr

#-------------------------------Selection Sort Code End-----------------------------#



# 3. Insertion sort

#-------------------------------Key Analysis-----------------------------#

# time complexity: {no of swap [n(n-1)/2)] + no of comparisons[n(n-1)/2)] }

#               (Worst case): O(n**2)     
#               (Best case) : O(n**2)           
#               (Avg case)  : O(n**2)

# space complexity:
#               (worst case): O(1)

# Stable Algorithms: Yes
# Adaptive:Yes 

#       Note:
#           1. Useful for Linked List.
#           2. It divides array in two parts.(sorted and unsorted)
#           3. No of pass requires n-1.
#           3. Data is partially sorted.

#-------------------------------Insertion Sort Code Start-----------------------------#

def Insertion_sort(arr:list)->list:
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key =arr[i]
        while (j>=0 & arr[j]>arr[i]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#-------------------------------Insertion Sort Code End-----------------------------#


# 4. Merge sort

#-------------------------------Key Analysis-----------------------------#

# time complexity: {no of swap [n(n-1)/2)] + no of comparisons[n(n-1)/2)] }

#               (Worst case): O(n**2)     
#               (Best case) : O(n**2)           
#               (Avg case)  : O(n**2)

# space complexity:
#               (worst case): O(1)

# Stable Algorithms: Yes
# Adaptive:Yes 

#       Note:
#           1. Useful for Linked List.
#           2. It divides array in two parts.(sorted and unsorted)
#           3. No of pass requires n-1.

#-------------------------------Merge Sort Code Start-----------------------------#

def Merge_sort(arr:list)->list:
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key =arr[i]
        while (j>=0 & arr[j]>arr[i]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#-------------------------------Merge Sort Code End-----------------------------#


# 4. Shell sort

#-------------------------------Key Analysis-----------------------------#

# time complexity: {no of swap [n(n-1)/2)] + no of comparisons[n(n-1)/2)] }

#               (Worst case): O(n**2)     
#               (Best case) : O(n**2)           
#               (Avg case)  : O(n**2)

# space complexity:
#               (worst case): O(1)

# Stable Algorithms: Yes
# Adaptive:Yes 

#       Note:
#           1. Useful for Linked List.
#           2. It divides array in two parts.(sorted and unsorted)
#           3. No of pass requires n-1.

#-------------------------------Shell Sort Code Start-----------------------------#

def Shell_sort(arr:list)->list:
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key =arr[i]
        while (j>=0 & arr[j]>arr[i]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#-------------------------------Shell Sort Code End-----------------------------#






#------------main function-------------------#


if __name__=='__main__':
    arr=[5,9,7,4,3,8,1]
    
    print("Original array: ")
    print(arr)
    print()
    print("array after applying bubble sort: ")
    print(Bubble_sort(arr))
    print()
    print("array after applying Selection sort: ")
    print(Selection_sort(arr))
    print()
    print("array after applying Insertion sort: ")
    print(Insertion_sort(arr))
    print()
