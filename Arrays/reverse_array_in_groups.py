# Given an array, reverse every sub-array formed by consecutive k elements.

# Input:

# The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of an integer N, where N is the size of array.The second line of each test case contains N space separated integers denoting array elements.The third line of each test case consists of an integer K.

# Output:
# Corresponding to each test case, in a new line, print the modified array.

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 500
# 1 ≤ A[i] ≤ 500

# Example:

# Input
# 1
# 5
# 1 2 3 4 5
# 3

# Output
# 3 2 1 5 4

def max_index_arr(arr,s,e):
    max_i = s
    for i in range(s,e+1):
        if arr[i]>arr[max_i]:
            max_i = i
    return max_i
        

def reverse_in_group(arr,n,k):
    start = 0
    while(start<n):
        # swap elements
        i = start
        j = min(start+k-1,n-1)
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1 
            j = j - 1
        start = start + k
    for item in arr:
        print(item,end=" ")
    print()

        
        

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    k = int(input())
    reverse_in_group(arr,n,k)