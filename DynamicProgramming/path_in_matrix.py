"""
url : https://practice.geeksforgeeks.org/problems/path-in-matrix/0

Given a N X N  matrix Matrix[N][N] of positive integers.  There are only three possible moves from a cell Matrix[r][c].

1. Matrix[r+1][c]

2. Matrix[r+1][c-1]

3. Matrix[r+1][c+1]

Starting from any column in row 0, return the largest sum of any of the paths up to row N-1.

Input:
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the order of matrix. Next line contains N*N integers denoting the elements of the matrix in row-major form.

Output:
Output the largest sum of any of the paths starting from any cell of row 0 to any cell of row N-1. Print the output of each test case in a new line.

Constraints:
1<=T<=20
2<=N<=20
1<=Matrix[i][j]<=1000 (for all 1<=i<=N && 1<=j<=N)

Example:

Input:
1
2
348 391 618 193

Output:
1009
"""

def path_in_matrix(matrix,n,i,j):
    if i>= n or j>= n:
        return -1000
    if i == n-1:
        return matrix[i][j]
    
    return matrix[i][j] + max(path_in_matrix(matrix,n,i+1,j-1),path_in_matrix(matrix,n,i+1,j),path_in_matrix(matrix,n,i+1,j+1))
    

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip(" ").split(" ")]
        matrix = []
        for i in range(0,n):
            index = n * i
            row = [arr[index + x] for x in range(0,n)]
            matrix.append(row)
        # print(matrix)
        max_path = 0
        for k in range(0,len(matrix)):
            max_path = max(max_path,path_in_matrix(matrix,n,0,k))
        print(max_path)

if __name__ == '__main__':
    main()
    