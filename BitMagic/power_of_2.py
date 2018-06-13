# Given a positive integer N, check if N is a power of 2.

# Input:
# The first line contains 'T' denoting the number of test cases. Then follows description of test cases.
# Each test case contains a single positive integer N.


# Output:
# Print "YES" if it is a power of 2 else "NO". (Without the double quotes)


# Constraints:
# 1<=T<=100
# 0<=N<=10^18

# Example:
# Input :
# 2
# 1
# 98

# Output :
# YES
# ​NO

def power_of_2(n):
    if n & (n-1) == 0:
        print("YES")
    else:
        print("NO")


#input 

t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers.split()[0])
    power_of_2(n)