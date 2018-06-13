# Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer 'N' denoting the size of array and the size of subarray 'k'.
# The second line contains 'N' space-separated integers A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print the maximum for every subarray of size k.

# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 100
# 1 ≤ k ≤ N
# 0 ≤A[i]<1000

# Example:

# Input:
# 2
# 9 3
# 1 2 3 1 4 5 2 3 6
# 10 4
# 8 5 10 7 9 4 15 12 90 13

# Output:
# 3 3 4 5 5 5 6
# 10 10 10 15 15 90 90

def max_index_arr(arr,s,e):
    max_i = s
    for i in range(s,e+1):
        if arr[i]>arr[max_i]:
            max_i = i
    return max_i
        

def maximum_of_subarray(arr,n,k):
    
    if k>=n:
        print(arr[max_index_arr(arr,0,n-1)])
        return
    
    result = []
    max_index = max_index_arr(arr,0,k-2)
    for i in range(k-1,n):
        if i-k == max_index or arr[max_index] < arr[i]:
            max_index = max_index_arr(arr,max_index+1,i)
        result.append(arr[max_index])
    
    for item in result:
        print(item,end=" ")
    print()
    return

t = int(input())

for i in range(0,t):
    numbers = input().strip().split()
    n = int(numbers[0])
    k = int(numbers[1])
    arr = [int(x) for x in input().strip().split(" ")]
    maximum_of_subarray(arr,n,k)