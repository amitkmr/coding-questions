# Given a number, check whether it is sparse or not. A number is said to be a sparse number if in binary representation of the number no two or more consecutive bits are set.

# Input:
# The first line of input contains an integer T denoting the number of test cases. The first line of each test case is number 'N'.

# Output:
# Print '1' if the number is sparse and '0' if the number is not sparse.

# Constraints:
# 1 <=T<= 100
# 1 <=n<= 100

# Example:
# Input:
# 2
# 2
# 3

# Output:
# 1
# 0



def is_sparse(n):
    if n & n>>1 == 0:
        print(1)
    else:
        print(0)

t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers)
    is_sparse(n)