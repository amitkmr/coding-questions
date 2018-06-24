"""
url : https://practice.geeksforgeeks.org/problems/edit-distance/0

Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.

Insert
Remove
Replace
All of the above operations are of cost=1.
Both the strings are of lowercase.

Input:
The First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each tese case consists of two lines. The first line of each test case consists of two space separated integers P and Q denoting the length of the strings str1 and str2 respectively. The second line of each test case coantains two space separated strings str1 and str2 in order.


Output:
Corresponding to each test case, pirnt in a new line, the minimum number of operations required.

Constraints:
1<=T<=50
1<= Length(str1) <= 100
1<= Length(str2) <= 100
 

Example:
Input:
1
4 5
geek gesek

Output:
1

"""

def lcs(str1,str2,i,j,matrix):
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    if matrix[i][j] != -1:
        return matrix[i][j]
    
    if str1[i] == str2[j]:
        matrix[i][j] = lcs(str1,str2,i-1,j-1,matrix)
        return matrix[i][j]
    matrix[i][j] = 1 + min(lcs(str1,str2,i-1,j,matrix),lcs(str1,str2,i,j-1,matrix),lcs(str1,str2,i-1,j-1,matrix))
    return matrix[i][j]

def main():
    t = int(input())

    for i in range(0,t):
        numbers = input().replace("  "," ").strip(" ").split(" ")
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        strings = input().strip(" ").split(" ")
        str1 = strings[0]
        str2 = strings[1]
        matrix = []
        for i in range(0,n1):
            row = [-1]*n2
            matrix.append(row)
        print(lcs(str1,str2,n1-1,n2-1,matrix))

if __name__ == '__main__':
    main()