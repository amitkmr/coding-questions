# Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N,N is the size of array.
# The second line of each test case contains N input A[].

# Output:

# Print the sum of maximum sum sequence of the given array.

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 100
# 1 ≤ A[] ≤ 1000

# Example:

# Input:
# 2
# 7
# 1 101 2 3 100 4 5
# 4
# 10 5 4 3

# Output:
# 106
# 10

# Explanation:
# For input:
# 7
# 1 101 2 3 100 4 5
# All the increasing subsequences : (1,101); (1,2,3,100); (1,2,3,4,5), out of this (1,2,3,100) has maximum sum,i.e., 106. Hence the output is stated as 106.

def maximum_sum_subsequence(arr,n):
    
    subsequence_sum = [0]*len(arr)
    for i in range(0,n):
        if i == 0 :
            subsequence_sum[i] = arr[i]
            continue
        j = i-1
        subsequence_sum[i] = arr[i]
        while(j>-1):
            if arr[j]<arr[i] and subsequence_sum[j]+arr[i]>subsequence_sum[i]:
                subsequence_sum[i] = subsequence_sum[j]+arr[i]
            j = j-1
    return max(subsequence_sum)
         

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    print(maximum_sum_subsequence(arr,n))