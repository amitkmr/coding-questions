# You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is a and b.

# Output:

# Print the number of bits needed to be flipped.

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ a,b ≤ 1000

# Example:

# Example:
# Input
# 1
# 10 20

# Output
# 4
 

# Explanation:

# A  = 1001001
# B  = 0010101
# No of bits need to flipped = set bit count i.e. 4You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is a and b.

# Output:

# Print the number of bits needed to be flipped.

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ a,b ≤ 1000

# Example:

# Example:
# Input
# 1
# 10 20

# Output
# 4
 

# Explanation:

# A  = 1001001
# B  = 0010101
# No of bits need to flipped = set bit count i.e. 4


def bit_difference(a,b):
    xor = a^b
    # count the set bits
    count = 0
    while(xor>0):
        if xor&1 == 1:
            count = count + 1
        xor = xor>>1
    return count

#input 

t = int(input())
for i in range(0,t):
    numbers = input()
    a = int(numbers.split()[0])
    b = int(numbers.split()[1])
    print(bit_difference(a,b))