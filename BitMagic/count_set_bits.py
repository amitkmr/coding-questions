# Find the sum of all bits from numbers 1 to N.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is N.

# Output:

# Print the sum of all bits.

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000

# Example:

# Input:
# 2
# 4
# 17

# Output:
# 5
# 35

# Explanation:
# An easy way to look at it is to consider the number, n = 4:
# 0 0 0 = 0
# 0 0 1 = 1
# 0 1 0 = 1
# 0 1 1 = 2
# 1 0 0 = 1
# Therefore , the total number of bits is 5

def count_bits(n):
    s = 0
    while(n>0):
        s = s + n & 1
        n = n>>1
    return s

t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers)
    print(count_bits(n))