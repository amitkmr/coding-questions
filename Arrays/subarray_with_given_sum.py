# Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

# Input:

# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

# Output:

# Corresponding to each test case, in a new line, print the starting and ending positions of first such occuring subarray if sum equals to subarray, else print -1.

# Note: Position of 1st element of the array should be considered as 1.

# Expected Time Complexity: O(n)

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 100
# 1 ≤ an array element ≤ 200

# Example:

# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10

# Output:
# 2 4
# 1 5

# Explanation : 
# In first test case, sum of elements from 2nd position to 4th position is 12
# In second test case, sum of elements from 1st position to 5th position is 15

def subarray_with_given_sum(arr,n,s):
    start = 0
    current_sum = 0
    for i in range(0,n):
        current_sum = current_sum + arr[i]
        while(current_sum > s):
            current_sum = current_sum -arr[start]
            start = start + 1
        if current_sum == s:
            print(start+1,i+1)
            return
    print(-1) 
    return

t = int(input())

for i in range(0,t):
    numbers = input().strip().split()
    n = int(numbers[0])
    s = int(numbers[1])

    arr = [int(x) for x in input().strip().split(" ")]
    subarray_with_given_sum(arr,n,s)

