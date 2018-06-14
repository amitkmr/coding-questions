"""

Given a string S, find the longest palindromic substring in S.
Substring of string S:

S[ i . . . . j ] where 0 ≤ i ≤ j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Input:

The first line of input consists number of the test cases. The following T lines consist of a string each.


Output:

In each separate line print the longest palindrome of the string given in the respective test case.


Constraints:

1 ≤T≤ 100
1 ≤ str≤ 100


Example:

Input:

1
aaaabbaa

Output:

aabbaa

"""

def max(str1,str2):
    if len(str1) < len(str2):
        return str2
    else:
        return str1

def longest_palindrome(string,s,e,matrix):
    
    if matrix[s][e] != "":
        return matrix[s][e]
    
    i = s
    j = e

    while(i<j):
        if string[i] == string[j]:
            i = i + 1
            j = j - 1
        else:
            return max(longest_palindrome(string,s,e-1,matrix),longest_palindrome(string,s+1,e,matrix))
    matrix[s][e] = string[s:e+1]
    return string[s:e+1]
        

t = int(input())
for i in range(0,t):
    string = input()
    matrix = [[""]*(len(string))] * len(string)
    print(longest_palindrome(string,0,len(string)-1,matrix))