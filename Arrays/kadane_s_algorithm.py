# Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
 
# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
 
# Output:
# Print the maximum sum of the contiguous sub-array in a separate line for each test case.
 
# Constraints:
# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 1000
# -100 ≤ A[i] <= 100
 
# Example:
# Input
# 2
# 3
# 1 2 3
# 4
# -1 -2 -3 -4
# Output
# 6
# -1

def kadane_algorithm(arr):
    _sum = -1000
    max_sum = -1000;
    for item in arr:
        _sum = max(_sum,0) + item
        if _sum > max_sum:
            max_sum = _sum
    return max_sum  

t = int(input())

for i in range(0,t):
    n = int(input())
    # print
    arr = [int(x) for x in input().strip().split(" ")]
    print(kadane_algorithm(arr))
    