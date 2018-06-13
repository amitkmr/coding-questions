# Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.

# The result is going to be very large, hence return the result in the form of a string.

# Input:

# The first line of input consists number of the test cases. The description of T test cases is as follows:

# The first line of each test case contains the size of the array, and the second line has the elements of the array.


# Output:

# In each separate line print the largest number formed by arranging the elements of the array in the form of a string.


# Constraints:

# 1 ≤ T ≤ 70
# 1 ≤ N ≤ 100
# 0 ≤ A[i] ≤ 1000


# Example:

# Input:

# 2
# 5
# 3 30 34 5 9
# 4
# 54 546 548 60

# Output:

# 9534330
# 6054854654

import functools

def compare(a,b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    return ba-ab
    
def largestNumber(A):
    sorted_a = sorted(A,key=functools.cmp_to_key(compare))
    return int("".join([str(i) for i in sorted_a]))

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    print(largestNumber(arr))