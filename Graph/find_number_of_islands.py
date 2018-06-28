"""
url : https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1

A group of connected 1s forms an island now your task is to complete the method findIslands which returns the no of islands present. The function  takes three arguments the first is the boolean matrix A and then the next two arguments are N and M denoting the size of the matrix A . 

Input:
The first line of input will be the no of test cases T then T test cases follow. The first line of each test case contains Two space separated integers N and M. Then in the next line are the NxM inputs of the matrix A separated by space .

Output:
The output in the expected output will be the total no of islands present. 

Constraints:
1<=T<=100
1<=N,M<=50
0<=A[][]<=1

Example(To be used only for expected output) :
Input
1
3 3
1 1 0 0 0 1 1 0 1
Output
2

Explanation
The graph will look like
1 1 0
0 0 1
1 0 1
Here  two islands will be formed
First island will be formed by elements { A[0][0] ,  A[0][1], A[1][2], A[2][2] }
Sec island will be formed by  { A[2][0] } 

"""
# Your code goes here
def main():
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findIslands(matrix, n[0], n[1]))
# Contrubuted By: Harshit Sidhwa


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# Your function should return an integer

def max(matrix,n,m):
    max_item = 0
    for i in range(n):
        for j in range(m):
            if max_item <matrix[i][j] :
                max_item = matrix[i][j]
    return max_item
    

def bfs(i,j,n,m,matrix,count):
    if i < 0 or i >= n or j < 0 or j>=m:
        return
    if matrix[i][j] == 1:
        matrix[i][j] = count
        bfs(i-1,j,n,m,matrix,count)
        bfs(i+1,j,n,m,matrix,count)
        bfs(i,j-1,n,m,matrix,count)
        bfs(i,j+1,n,m,matrix,count)

        # diagonal
        bfs(i-1,j-1,n,m,matrix,count)
        bfs(i-1,j+1,n,m,matrix,count)
        bfs(i+1,j-1,n,m,matrix,count)
        bfs(i+1,j+1,n,m,matrix,count)


def findIslands(matrix, n, m):
    count = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                count = count + 1
                bfs(i,j,n,m,matrix,count)
    result =  max(matrix,n,m)-1
    if result == -1:
        return 0
    else:
        return result
if __name__ == '__main__':
    main()
    
