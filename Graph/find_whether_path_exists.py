"""
url : https://practice.geeksforgeeks.org/problems/find-whether-path-exist/0

Given a N X N matrix (M) filled with 1 , 0 , 2 , 3 . Your task is to find whether there is a path possible from source to destination, while traversing through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
Note : there is only single source and single destination.
 

Examples:

Input : M[3][3] = {{ 0 , 3 , 2 },
                   { 3 , 3 , 0 },
                   { 1 , 3 , 0 }};
Output : Yes

Input : M[4][4] = {{ 0 , 3 , 1 , 0 },
                   { 3 , 0 , 3 , 3 },
                   { 2 , 3 , 0 , 3 },
                   { 0 , 3 , 3 , 3 }};
Output : Yes


Input:
The first line of input is an integer T denoting the no of test cases. Then T test cases follow. Each test case consists of 2 lines . The first line of each test case contains an integer N denoting the size of the square matrix . Then in the next line are N*N space separated values of the matrix (M) .

Output:
For each test case in a new line print 1 if the path exist from source to destination else print 0.

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
4
3 0 0 0 0 3 3 0 0 1 0 3 0 2 3 3 
3
0 3 2 3 0 0 1 0 0
Output:
1
0

"""

def is_destination(n,i,j,matrix):
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if matrix[i][j] == 2:
        return True
    if matrix[i][j] == 3 or matrix[i][j] == 1:
        matrix[i][j] = 4
        return is_destination(n,i+1,j,matrix) or is_destination(n,i,j+1,matrix) or is_destination(n,i-1,j,matrix) or is_destination(n,i,j-1,matrix)
    return False

def find_if_path_exists(n,matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if is_destination(n,i,j,matrix):
                    return 1
    return 0

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        matrix_arr = [int(x) for x in input().strip(" ").split(" ")]
        matrix = []
        for j in range(n):
            matrix.append(matrix_arr[j*n:(j+1)*n])
        print(find_if_path_exists(n,matrix))
    
if __name__ == '__main__':
    main()
    