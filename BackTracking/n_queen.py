"""
https://practice.geeksforgeeks.org/problems/n-queen-problem/0


            
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. Given an integer n, print all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the chessboard.

Output:
For each test case, output your solutions on one line where each solution is enclosed in square brackets '[', ']' separated by a space . The solutions are permutations of {1, 2, 3 …, n} in increasing order where the number in the ith place denotes the ith-column queen is placed in the row with that number, if no solution exists print -1.

Constraints:
1<=T<=10
1<=n<=10

Example:
Input
2
1
4
Output:
[1 ]
[2 4 1 3 ] [3 1 4 2 ]

"""

def check_column(matrix,i,j):
    for k in range(i,-1,-1):
        if matrix[k][j] == 1:
            return True
    return False

def check_diagonal(matrix,i,j,n):
    if i<0 or i>=n or j<0 or j>= n:
        return False
    
    # left_side
    left = j
    right = j
    for i in range(i-1,-1,-1):
        left = left - 1
        right = right + 1
        if left >=0 and matrix[i][left] == 1:
            return True
        
        if right <n and matrix[i][right] == 1:
            return True
        
    return False

def add_matrix_to_array(matrix,n,result):
    arr = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                arr.append(j+1)
    result.append(arr)

def reset_matrix(matrix,n,i):
    for k in range(i,n):
        matrix[k] = [0]*n

def n_queen(matrix,n,i,result):
    if i == n:
        add_matrix_to_array(matrix,n,result)
        return
    for j in range(n):
        if not check_diagonal(matrix,i,j,n) and not check_column(matrix,i,j):
            matrix[i][j] = 1
            n_queen(matrix,n,i+1,result)
            reset_matrix(matrix,n,i)

def print_different_soluttion(n):
    result = []
    matrix = []
    for j in range(n):
        matrix.append([0]*n)
    n_queen(matrix,n,0,result)

    for item in result:
        print(item,end=" ")
    print()
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print_different_soluttion(n)

if __name__ == '__main__':
    main()
    