"""          
The task is to complete partition() function which is used to implement Quick Sort.

Input:
First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.


Output:
Sorted array in increasing order is displayed to the user.


Constraints:
1 <=T<= 50
1 <=N<= 1000
1 <=arr[i]<= 1000


Example:

Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10
"""

def partition(arr,p,r):
    pivot = arr[r]

    for i in range(p,r):
        if arr[i]<pivot:
            continue
        
        j = i + 1 
        while(j<r and arr[j]>pivot):
            j = j+1
        arr[i],arr[j] = arr[j],arr[i]
        if j == r:
            return i
    return r            
            

def qsort(arr,p,r):
    if p >= r:
        return   

    q = partition(arr,p,r)
    qsort(arr,p,q-1)
    qsort(arr,q+1,r)

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    qsort(arr,0,n-1)
    print(" ".join([str(x) for x in arr]))