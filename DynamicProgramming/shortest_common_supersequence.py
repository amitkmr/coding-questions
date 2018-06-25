"""
url:https://practice.geeksforgeeks.org/problems/shortest-common-supersequence/0
Given two strings str1 and str2, find the shortest common shortest common subsequence of the two strings.

Input:
The first line of input contains an integer T denoting the number of test cases.Each test case contains two space separated strings.

Output:
Output the length of the shortest common supersequence.

Constraints:
1<=T<=100

Example:
Input:
2
abcd xycd
efgh jghi
Output:
6
6
"""
def lcs(str1,str2,i,j,matrix):
    if i<0 or j < 0:
        return 0
    if matrix[i][j] != -1:
        return matrix[i][j]
    
    if str1[i] == str2[j]:
        matrix[i][j] = 1 + lcs(str1,str2,i-1,j-1,matrix)
        return matrix[i][j]
    matrix[i][j] = max(lcs(str1,str2,i-1,j,matrix),lcs(str1,str2,i,j-1,matrix))
    return matrix[i][j]

def main():
    t = int(input())
    for i in range(0,t):
        strings = input().strip(" ").split(" ")
        str1 = strings[0]
        str2 = strings[1]
        matrix = []
        for i in range(0,len(str1)):
            row = [-1]*len(str2)
            matrix.append(row)
        print(len(str1)+len(str2)-lcs(str1,str2,len(str1)-1,len(str2)-1,matrix))

if __name__ == '__main__':
    main()
    
