"""
url : https://practice.geeksforgeeks.org/problems/shortest-source-to-destination-path/0

Given a boolean 2D matrix (0-based index), find whether there is path from (0,0) to (x,y) and 
if there is one path, print the minimum no of steps needed to reach it, else print -1 if the 
destination is not reachable. You may move in only four direction ie up, down, left and right. 
The path can only be created out of a cell if its value is 1.

Input:
The first line of input contains an integer T denoting the no of test cases. 
Then T test cases follow. Each test case contains two lines . The first line of each test 
case contains two integers n and m denoting the size of the matrix. Then in the next line 
are n*m space separated values of the matrix. The following line after it contains two integers 
x and y denoting the index of the destination.

Output:
For each test case print in a new line the min no of steps needed to reach the destination.

Constraints:
1<=T<=100
1<=n,m<=20

Example:
Input:
2
3 4
1 0 0 0 1 1 0 1 0 1 1 1
2 3
3 4
1 1 1 1 0 0 0 1 0 0 0 1
0 3
Output:
5
3

"""

def next_step(matrix,i,j,x,y,n,m):
    if i <0 or j<0 or i>=n or j >= m:
        return 100
    if matrix[i][j] == 0:
        return 100
    if i == x and j == y:
        return 0
    matrix[i][j] = 0 
    return 1 + min(next_step(matrix,i+1,j,x,y,n,m),next_step(matrix,i,j+1,x,y,n,m),next_step(matrix,i-1,j,x,y,n,m),next_step(matrix,i,j-1,x,y,n,m))

def shortest_path(x,y,n,m,matrix):
    result = next_step(matrix,0,0,x,y,n,m)
    if result >=100:
        print(-1)
    else:
        print(result)

def main():
    t = int(input())
    for i in range(t):
        numbers = input().strip(" ").split(" ")
        n = int(numbers[0])
        m = int(numbers[1])
        matrix_arr = [int(x) for x in input().strip(" ").split(" ")]
        matrix = []

        for j in range(n):
            matrix.append(matrix_arr[j*m:(j+1)*m])
        x_y = input().strip(" ").split(" ")
        x = int(x_y[0])
        y = int(x_y[1])
        shortest_path(x,y,n,m,matrix)

if __name__ == '__main__':
    main()
    