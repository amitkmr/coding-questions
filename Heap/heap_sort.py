"""
url : https://practice.geeksforgeeks.org/problems/heap-sort/1
The task is to complete heapify() and buildHeap() functions which are used to implement Heap Sort. 

Input:
First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.


Output:
Sorted array in ascending order.


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

def left(i):
    return 2*i+1
def right(i):
    return 2*i +2

def max_headpify(arr,i):
    max_index = i

    if left(i)<len(arr) and arr[i] < arr[left(i)]:
        max_index = left(i)
    
    if right(i)<len(arr) and arr[max_index] < arr[right(i)]:
        max_index = right(i)

    if i != max_index:
        arr[i],arr[max_index] = arr[max_index],arr[i]
        max_headpify(arr,max_index)  

def heapsort(arr,n):
    for i in range(0,int(n/2)):
        j = int(n/2) - i
        max_headpify(arr,j)

t = int(input())
for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    heapsort(arr,n)
    print(arr)

