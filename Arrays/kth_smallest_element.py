# Given an array and a number k where k is smaller than size of array, the task is to find the k’th smallest element in the given array. It is given that all array elements are distinct.

# Input:

# First Line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

# Output:

# Corresponding to each test case, print the desired output in a new line.

# Constraints:

# 1<=T<=200
# 1<=N<=1000
# K

# Expected Time Complexity: O(n)

# Example:

# INPUT
# 2
# 6
# 7 10 4 3 20 15
# 3
# 5
# 7 10 4 20 15
# 4

# Output:

# 7
# 15

def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def heapify(arr,i):
    n = len(arr)
    small_index = i
    if left(i) < n  and arr[left(i)] < arr[small_index]:
        small_index = left(i)
    if right(i) < n  and arr[right(i)] < arr[small_index]:
         small_index = right(i)
    # if small index is different then swap
    if small_index != i:
        arr[small_index],arr[i] = arr[i],arr[small_index]
        return heapify(arr,small_index)
    return arr

def make_heap(arr,n):
    index = int(n/2)
    while(index > -1):
        arr = heapify(arr,index)
        index = index - 1
    return arr

def kth_smallest_element(arr,n,k):
    arr = make_heap(arr,n)
    while(k>1 and n>1):
        arr[0],arr[n-1] = arr[n-1],arr[0]
        del(arr[n-1])
        arr = heapify(arr,0)
        k = k-1
        n = n-1
    return arr[0]


t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    k = int(input())
    print(kth_smallest_element(arr,n,k))