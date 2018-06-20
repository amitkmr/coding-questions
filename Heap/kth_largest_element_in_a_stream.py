"""
Given an input stream of n integers the task is to insert integers to stream and print the kth largest element in the stream at each insertion.

Example:

Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output:    {-1,   -1, 10, 11, 20, 40, 50,  50, ...}

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of each test case contains two space separated integers k and n . Then in the next line are n space separated values of the array.

Output:
For each test case in a new line print the space separated values denoting the kth largest element at each insertion, if the kth largest element at a particular insertion in the stream doesn't exist print -1.

Constraints:
1<=T<=100
1<=n,k<=1000
1<=stream[]<=100000

Example:
Input:
2
4 6
1 2 3 4 5 6
1 2
3 4 

Output:
-1 -1 -1 1 2 3
3 4 

"""

def parent(i):
    return int((i-1)/2)
def left(i):
    return 2*i+1
def right(i):
    return 2*i +2

def min_heap_up(arr,i):
    if arr[i]<arr[parent(i)]:
        arr[i],arr[parent(i)] = arr[parent(i)],arr[i]
        min_heap_up(arr,parent(i))

def min_headpify(arr,i):
    min_index = i

    if left(i)<len(arr) and arr[i]>arr[left(i)]:
        min_index = left(i)
    
    if right(i)<len(arr) and arr[min_index] > arr[right(i)]:
        min_index = right(i)

    if i != min_index:
        arr[i],arr[min_index] = arr[min_index],arr[i]
        min_headpify(arr,min_index)


def insert_min_heap(min_heap,item):
    min_heap.append(item)
    min_heap_up(min_heap,len(min_heap)-1)

def kth_largest(arr,n,k):
    min_heap = []
    for i in range(0,n):
        if i < k-1:
            insert_min_heap(min_heap,arr[i])
            print("-1",end=" ")
            continue
        if i == k-1:
            insert_min_heap(min_heap,arr[i])
            print(min_heap[0],end=" ")
            continue
        if arr[i] > min_heap[0]:
            min_heap[0] = arr[i]
            min_headpify(min_heap,0)
        print(min_heap[0],end=" ")
    print()

t = int(input())
for i in range(0,t):
    numbers = input().strip().split(" ")
    k = int(numbers[0])
    n = int(numbers[1])
    arr = [int(x) for x in input().strip().split(" ")]
    kth_largest(arr,n,k)