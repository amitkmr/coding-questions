"""
url : https://practice.geeksforgeeks.org/problems/longest-common-substring-value-of-two-numbers/0
Given two integers N and M. The task is to find the longest contiguous subset in binary representation of both the numbers and print its decimal value.

Note: If there are two or more longest common substrings with the same length, the print the maximum value of all the common substrings.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two integer N and M as input.

Output:
For each test case, print the decimal value of longest common substring In new line.

Constraints:
1<=T<=1000
1<=N,M<=1018

Example:
Input:
2
10 11
8 16

Output:
5
8
"""


def print_matrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j],end=" ")
        print()
    


def matrix_val(matrix,i,j):
    if i<0 or j<0:
        return 0
    else:
        return matrix[i][j]

def longest_common_substring(str1,str2,matrix):
    n = len(str1)
    m = len(str2)
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix_val(matrix,i-1,j-1) + 1

def max_common_string_number(str1,str2):
    n = len(str1)
    m = len(str2)
    
    matrix = []
    for i in range(n):
        matrix.append([0]*m)
    longest_common_substring(str1,str2,matrix)

    # print_matrix(matrix,n,m)

    max_val = 0
    max_len = 0
    i  = 0
    for item in matrix:
        length = max(item)
        val = int(str1[i-length+1:i+1],2)
        if max_len < length:
            max_len = length
            max_val = val
        
        if max_len == length:
            if max_val < val:
                max_val = val
        i+=1
    print(max_val)
            

def main():
    t = int(input())
    for i in range(t):
        n1,n2 = list(map(int,input().split()))
        b1 = bin(n1).split('b')[1]
        b2 = bin(n2).split('b')[1]
        max_common_string_number(b1,b2)    
if __name__ == '__main__':
    main()
    
    
    
            