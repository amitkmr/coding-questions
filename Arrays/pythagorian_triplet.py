# Pythagorean Triplet
# Submissions: 13057   Accuracy: 33.36%   Difficulty: Easy
        
# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

# Input:
# The first line contains 'T' denoting the number of testcases. Then follows description of testcases.
# Each case begins with a single positive integer N denoting the size of array.
# The second line contains the N space separated positive integers denoting the elements of array A.

# Output:
# For each testcase, print "Yes" or  "No" whtether it is Pythagorean Triplet or not.

# Constraints:
# 1<=T<=50
#  1<=N<=100
#  1<=A[i]<=100

# Example:
# Input:
# 1
# 5
# 3 2 4 6 5
# Output:
# Yes


def trapping_rain_water(arr,n):

    for i in range(0,n):
        arr[i] = arr[i]*arr[i]
    
    arr = sorted(arr)

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j] in arr:
                print("Yes")
                return
    print("No")

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    trapping_rain_water(arr,n)