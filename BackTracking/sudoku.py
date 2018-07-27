"""
https://practice.geeksforgeeks.org/problems/solve-the-sudoku/0

Given an incomplete Sudoku configuration in terms of a 9x9  2-D square matrix (mat[][]) the task to print a solution of the Sudoku. For simplicity you may assume that there will be only one unique solution.

Example


For the above configuration the solution is
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 9*9 space separated values of the matrix mat[][] representing an incomplete Sudoku state where a 0 represents empty block.

Output:
For each test case in a new line print the space separated values of the solution of the the sudoku.

Constraints:
1<=T<=10
0<=mat[]<=9

Example:
Input:
1
3 0 6 5 0 8 4 0 0 5 2 0 0 0 0 0 0 0 0 8 7 0 0 0 0 3 1 0 0 3 0 1 0 0 8 0 9 0 0 8 6 3 0 0 5 0 5 0 0 9 0 6 0 0 1 3 0 0 0 0 2 5 0 0 0 0 0 0 0 0 7 4 0 0 5 2 0 6 3 0 0

Output:
3 1 6 5 7 8 4 9 2 5 2 9 1 3 4 7 6 8 4 8 7 6 2 9 5 3 1 2 6 3 4 1 5 9 8 7 9 7 4 8 6 3 1 2 5 8 5 1 7 9 2 6 4 3 1 3 8 9 4 7 2 5 6 6 9 2 3 5 1 8 7 4 7 4 5 2 8 6 3 1 9
"""


def number_in_small_matrix(matrix,i,j,k):
    i = int(i/3)*3
    j = int(j/3)*3

    for l in range(3):
        for m in range(3):
            if matrix[i+l][j+m] == k:
                return True
    return False 

def in_column(matrix,j,k):
    for i in range(9):
        if k == matrix[i][j]:
            return True
    return False


def printMatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
    print()

def solve_sudoku(matrix,i,j):
    if j==9:
        i = i+1
        j = 0
    if i==9:
        return True
    
    if matrix[i][j] != 0:
        return solve_sudoku(matrix,i,j+1)

    for k in range(0,10):
        if k not in matrix[i] and not number_in_small_matrix(matrix,i,j,k) and not in_column(matrix,j,k):
            matrix[i][j] = k
            if solve_sudoku(matrix,i,j+1):
                return True
    
    matrix[i][j] = 0
    return False
            

def main():
    t = int(input())
    for i in range(t):
        matrix = []
        for i in range(9):
            matrix.append([-1]*9)
        matrix_arr = list(map(int,input().split()))
        count = 0
        for j in range(9):
            for k in range(9):
                matrix[j][k] = matrix_arr[count]
                count = count + 1
        
        solve_sudoku(matrix,0,0)
        printMatrix(matrix,9)
        
if __name__ == '__main__':
    main()