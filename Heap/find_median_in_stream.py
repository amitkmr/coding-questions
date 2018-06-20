"""
url : https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0
Given an input stream of n integers the task is to insert integers to stream and print the median of the new stream formed by each insertion of x to the stream.

Example

Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5)
15 goes to stream --> median 10 (5, 15)
1 goes to stream --> median 5 (5, 15, 1)
3 goes to stream --> median 4 (5, 15, 1, 3)

Input:
The first line of input contains an integer N denoting the no of elements of the stream. Then the next N lines contains integer x denoting the no to be inserted to the stream.

Output:
For each element added to the stream print the floor of the new median in a new line.

Constraints:
1<=N<=10^5+7
1<=x<=10^5+7

Example:
Input:
4
5
15
1 
3
Output:
5
10
5
4
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

def max_heap_up(arr,i):
    if arr[i] > arr[parent(i)]:
        arr[i],arr[parent(i)] = arr[parent(i)],arr[i]
        max_heap_up(arr,parent(i))

def min_headpify(arr,i):
    min_index = i

    if left(i)<len(arr) and arr[i]>arr[left(i)]:
        min_index = left(i)
    
    if right(i)<len(arr) and arr[min_index] > arr[right(i)]:
        min_index = right(i)

    if i != min_index:
        arr[i],arr[min_index] = arr[min_index],arr[i]
        min_headpify(arr,min_index)

def max_headpify(arr,i):
    max_index = i

    if left(i)<len(arr) and arr[i] < arr[left(i)]:
        max_index = left(i)
    
    if right(i)<len(arr) and arr[max_index] < arr[right(i)]:
        max_index = right(i)

    if i != max_index:
        arr[i],arr[max_index] = arr[max_index],arr[i]
        max_headpify(arr,max_index)

def insert_min_heap(min_heap,item):
    min_heap.append(item)
    min_heap_up(min_heap,len(min_heap)-1)    

def insert_max_heap(max_heap,item):
    max_heap.append(item)
    max_heap_up(max_heap,len(max_heap)-1) 

def find_median(min_heap,max_heap,number):
    if len(max_heap) == 0:
        insert_max_heap(max_heap,number)
        return number
    if len(min_heap) == 0:
        if number < max_heap[0]:
            insert_min_heap(min_heap,max_heap[0])
            max_heap[0] = number
        else:
            insert_min_heap(min_heap,number)
        return (max_heap[0] + min_heap[0])/2

    if number > max_heap[0] and number < min_heap[0]:
        if len(max_heap) == len(min_heap):
            insert_max_heap(max_heap,number)
            return number
        else:
            insert_min_heap(min_heap,number)
            return (max_heap[0] + min_heap[0])/2
    if number <= max_heap[0]:
        if len(max_heap)>len(min_heap):
            insert_min_heap(min_heap,max_heap[0])
            max_heap[0] = number
            max_headpify(max_heap,0)
            return (max_heap[0] + min_heap[0])/2
        else:
            insert_max_heap(max_heap,number)
            return max_heap[0]
    if number >= min_heap[0]:
        if len(max_heap)>len(min_heap):
            insert_min_heap(min_heap,number)
            return (max_heap[0] + min_heap[0])/2
        else:
            insert_max_heap(max_heap,min_heap[0])
            min_heap[0] = number
            min_headpify(min_heap,0)
            return max_heap[0]

t = int(input())
min_heap = []
max_heap = []
for i in range(0,t):
    item = int(input())
    print(find_median(min_heap,max_heap,item))
    print(max_heap)
    print(min_heap)