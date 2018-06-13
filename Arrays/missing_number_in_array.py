# Given an array of size n-1 and given that there are numbers from 1 to n with one missing, the missing number is to be found.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N.
# The second line of each test case contains N-1 input C[i],numbers in array.

# Output:

# Print the missing number in array.

# Constraints:

# 1 ≤ T ≤ 200
# 1 ≤ N ≤ 1000
# 1 ≤ C[i] ≤ 1000

# Example:

# Input
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10

# Output
# 4
# 9

def missing_number_in_array(arr,n):
    n_xor = 0

    for i in range(1,n+1):
        n_xor = n_xor^i 

    for item in arr:
        n_xor = n_xor^item
    return n_xor

t = int(input())

for i in range(0,t):
    n = int(input())

    arr = [int(x) for x in input().strip().split(" ")]
    print(missing_number_in_array(arr,n))
    