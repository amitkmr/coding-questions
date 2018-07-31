"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Examples :

Input : X = "GeeksforGeeks", y = "GeeksQuiz"
Output : 5
The longest common substring is "Geeks" and is of
length 5.

Input : X = "abcdxyz", y = "xyzabcd"
Output : 4
The longest common substring is "abcd" and is of
length 4.

Input : X = "zxabcdezy", y = "yzabcdezx"
Output : 6
The longest common substring is "abcdez" and is of
length 6.
 

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string X and Y respectively
The next two lines contains the 2 string X and Y.


Output:
For each test case print the length of longest  common substring of the two strings .


Constraints:
1<=T<=200
1<=size(X),size(Y)<=100


Example:
Input:
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Output:

4
1

"""

def common_string(str1,str2,i,j):
    if i<0 or j<0:
        return 0

    if str1[i] == str2[j]:
        return 1 + common_string(str1,str2,i-1,j-1)
    else:
        return 0    


def longest_common_substring(string1,string2,i,j,matrix):
    if i<0 or j<0:
        return 0
    if matrix[i][j] != -1:
        return matrix[i][j]

    matrix[i][j] = max(common_string(string1,string2,i,j),longest_common_substring(string1,string2,i-1,j-1,matrix),longest_common_substring(string1,string2,i-1,j,matrix),longest_common_substring(string1,string2,i,j-1,matrix))
    return matrix[i][j]
    
def lcs(string1,string2,n1,n2):
    
    matrix = []
    for i in range(0,len(string1)):
        row = [-1]*len(string2)
        matrix.append(row)
    
    print(longest_common_substring(string1,string2,n1-1,n2-1,matrix))

t = int(input())

for i in range(0,t):
    numers = input().strip().split(" ")
    n1 = int(numers[0])
    n2 = int(numers[1])

    string1 = input()
    string2 = input()
    lcs(string1,string2,n1,n2)