"""
url : https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0

Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .


Output:
For each test case print the length of longest  common subsequence of the two strings .


Constraints:
1<=T<=200
1<=size(str1),size(str2)<=100


Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2


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
        numbers = input().replace("  "," ").strip(" ").split(" ")
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        str1 = input()
        str2 = input()
        matrix = []
        for i in range(0,n1):
            row = [-1]*n2
            matrix.append(row)
        print(lcs(str1,str2,n1-1,n2-1,matrix))

if __name__ == '__main__':
    main()
    