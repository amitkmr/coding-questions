"""
https://practice.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string/0

Given a string, the task is to count all palindromic sub-strings present in it.

Input:

The first line of input will contain no of test cases T . Then T test cases follow . Each test case contains 2 lines. The first line of each test case contains an integer N denoting the length of the string, next line of test case contains the string


Output:

For each test case output a single line depecting the number of palindromic substrings present.


Constraints:

1<=T<=100
2<=N<=500


Example:

Input

2
5
abaab
7
abbaeae

Output

3
4

Explanation:

Test Case 1
Input : str = "abaab"
Output: 3
All palindrome substring are : "aba" , "aa" , "baab"

Test Case 2
Input : str = "abbaeae"
Output: 4
All palindrome substring are : "bb" , "abba" ,"aea","eae"

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

    # print_matrix(matrix,n,n)

def all_palindromes(matrix,n,st):
    
    result = []
    for i in range(n):
        for j in range(n):
            palin = ""
            k = 0
            while(i+k<n and j+k<n and matrix[i+k][j+k]!=0):
                matrix[i+k][j+k] = 0
                palin+=st[i+k]
                k+=1
            if k>1:
                result.append(palin)
        
    return result


def count_palindrome(st):
    str1 = st
    str2 = st[::-1]
    n = len(st)
    
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    longest_common_substring(str1,str2,matrix)

    # print_matrix(matrix,n,n)
    result = all_palindromes(matrix,n,st)

    count = 0
    for item in set(result):
        count+=len(item)//2

    print(count)
                
    

def main():
    t = int(input())
    for i in range(t):
        n = input()
        st = input()
        
        count_palindrome(st)

if __name__ == '__main__':
    main()