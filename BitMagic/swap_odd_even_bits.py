# Given an unsigned integer N, swap all odd bits with even bits. For example, if the given number is 23 ( 0 0 0 1 0 1 1 1 ), it should be converted to 43 ( 0 0 1 0 1 0 1 1 ). Here every even position bit is swapped with adjacent bit on right side (even position bits are highlighted in binary representation of 23), and every odd position bit is swapped with adjacent on left side.

# Input:

# The first line of input contains an integer T denoting the number of test cases.
# Then T test cases follow. The first line of each test case contains an integer N.

# Output:

# Corresponding to each test case, print in a new line, the converted number .

# Constraints:

# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 100

# Example:

# Input
# 2
# 23
# 2

# Output
# 43
# 1

def swap_bits(n):
    mask = 1

    while(mask<n):
        
        if mask & 1 == 1:
            mask = mask <<1
        else:
            mask = (mask<<1)|1
    odd_mask = 0
    even_mask = 0
    
    if mask & 1 == 1:
        odd_mask = n & mask
        even_mask = n & mask>>1
    else:
        odd_mask = n & mask>>1
        even_mask = n & mask
    even_mask = even_mask>>1
    odd_mask = odd_mask<<1
    print(even_mask|odd_mask)
             

t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers)
    swap_bits(n)
