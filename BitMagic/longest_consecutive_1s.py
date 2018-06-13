# Given a number N, Your task is to find the  length of the longest consecutive 1's in its binary representation.

# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.

# Output:
# For each test case in a new line print the length of the longest consecutive 1's in N's binary representation.

# Constraints:
# 1<=T<100
# 1<=N<=1000

# Example:
# Input
# 2
# 14
# 222
# Output
# 3 
# 4

#input 

def longest_consecutive1(n):
    current_length = 0
    max_length = 0
    while(n>0):
        if n&1 !=0:
            current_length = current_length + 1
        else:
            current_length = 0
            
        if current_length > max_length:
            max_length = current_length
        n = n>>1
    print(max_length)
    
t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers)
    longest_consecutive1(n)