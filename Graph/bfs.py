"""
url : https://practice.geeksforgeeks.org/problems/x-total-shapes/0
          
Given N * M string array of O's and X's
Return the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

Example (1):

OOOXOOO
OXXXXXO
OXOOOXO

answer is 1 , shapes are  :
(i)     X
    X X X X
    X     X
 

Example (2):

XXX
OOO
XXX

answer is 2, shapes are
(i)  XXX

(ii) XXX

Input:
The first line of input takes the number of test cases, T.
Then T test cases follow. Each of the T test cases takes 2 input lines.
The first line of each test case have two integers N and M.The second line of N space separated strings follow which indicate the elements in the array.

Output:

Print number of shapes.

Constraints:

1<=T<=100

1<=N,M<=50

Example:

Input:
2
4 7
OOOOXXO OXOXOOX XXXXOXO OXXXOOO
10 3
XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO

Output:
4
6

"""

def max(matrix,n,m):
    max_item = 0
    for i in range(n):
        for j in range(m):
            if max_item <matrix[i][j] :
                max_item = matrix[i][j]
    return max_item
    

def bfs(i,j,n,m,matrix,count):
    if i < 0 or i >= n or j < 0 or j>=m :
        return
    if matrix[i][j] == '0':
        matrix[i][j] = 0
        return
    if matrix[i][j] == 'X':
        matrix[i][j] = count
        bfs(i-1,j,n,m,matrix,count)
        bfs(i+1,j,n,m,matrix,count)
        bfs(i,j-1,n,m,matrix,count)
        bfs(i,j+1,n,m,matrix,count)
    

def x_total_shapes(matrix,n,m):
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'X':
                count = count + 1
                bfs(i,j,n,m,matrix,count)
            if matrix[i][j] == 'O':
                matrix[i][j] = 0
    print(max(matrix,n,m))                

def main():
    t = int(input())
    for i in range(t):
        numbers = input().strip(" ").split(" ")
        n = int(numbers[0])
        m = int(numbers[1])
        matrix_str = input().strip(" ").split(" ")
        matrix = []
        for item in matrix_str:
            matrix.append(list(item))
        x_total_shapes(matrix,n,m)

if __name__ == '__main__':
    main()
    