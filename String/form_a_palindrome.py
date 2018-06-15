"""

Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is S.

Output:

Print the minimum number of characters.

Constraints:

1 ≤ T ≤ 50
1 ≤ S ≤ 40

Example:

Input:
3
abcd
aba
geeks

Output:
3
0
3

"""

def form_a_palindrome(string,s,e,matrix):
    
    if e<s:
        return 0
    if e==s:
        matrix[s][e] = 0
        return matrix[s][e]
        # return 0

    if matrix[s][e] != -1:
        return matrix[s][e]
    if string[s] == string[e]:
        matrix[s][e] = form_a_palindrome(string,s+1,e-1,matrix) 
        return matrix[s][e]
    else:
        matrix[s][e] = 1 + min(form_a_palindrome(string,s,e-1,matrix),form_a_palindrome(string,s+1,e,matrix))
        return matrix[s][e]

t = int(input())

for i in range(0,t):
    string = input()
    matrix = []
    for i in range(0,len(string)):
        row = [-1]*len(string)
        matrix.append(row)
        
    print(form_a_palindrome(string,0,len(string)-1,matrix))
