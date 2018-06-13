# Given an integer N and an integer D, you are required to write a program to rotate the binary representation of the integer N by D digits to the left as well as right and print the results in decimal values after each of the rotation.

# Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000.....001100.

# Input:
# First line of input contains a single integer T which denotes the number of test cases. Each test case contains two space separated integers N and D where N denotes the number to be rotated and D denotes the number of digits by which the number is required to be rotated.

# Output:
# For first line of each test case prints the value of number N after rotating it to left by D digits and  second line prints the value of number N after rotating it to the right by D digits.

# Constraints:
# 1<=T<=100
# 1<=N<=1000
# 1<=D<=100

# Example:
# Input:
# 2
# 229 3
# 28 2
# Output:
# 47
# 188
# 19
# 7

def rotate_bits(n,d):
    binary_n = bin(n).split('b')[1]
    roated_num = binary_n[d:]+binary_n[:d]
    print(int(roated_num,2))
    l = len(binary_n) - d
    roated_num = binary_n[l:]+binary_n[:l]
    print(int(roated_num,2))

#input 

t = int(input())
for i in range(0,t):
    numbers = input()
    n = int(numbers.split()[0])
    d = int(numbers.split()[1])
    rotate_bits(n,d)
