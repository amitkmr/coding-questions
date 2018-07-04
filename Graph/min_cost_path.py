"""
url : https://practice.geeksforgeeks.org/problems/minimum-cost-path/0

Given a square grid of size n, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.

Note : It is assumed that negative cost cycles do not exist in input matrix.

Input:

The first line of input will contain number of test cases T . Then T test cases follow . Each test case contains 2 lines. The first line of each test case contains an integer n denoting the size of the grid. Next line of each test contains a single line containing N*N space separated integers depecting cost of respective cell from (0,0) to (n,n).


Output:

For each test case output a single integer depecting the minimum cost to reach the destination.


Constraints:

1<=T<=50
1<= n<= 50


Example:

Input

2
5
31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
2
42 93 7 14
 

Output
327
63

Explanation:

Test Case 1:

Grid is:
31, 100, 65, 12, 18,
10, 13, 47, 157, 6,
100. 113, 174, 11, 33,
88, 124, 41, 20, 140,
99, 32, 111, 41, 20

A cost grid is given in below diagram, minimum 
cost to reach bottom right from top left 
is 327 (= 31 + 10 + 13 + 47 + 65 + 12 + 18 + 
6 + 33 + 11 + 20 + 41 + 20)

"""
3


def min_path(matrix,distance,queue,i,j,n,m):
    x = [-1,0,0,1]
    y = [0,1,-1,0]
    
    for k in range(len(x)):
        x_vertex = i+x[k]
        y_vertex = j+y[k]

        if x_vertex <0 or x_vertex >= n or y_vertex < 0 or y_vertex >=m:
            continue
        if distance[x_vertex][y_vertex] > distance[i][j] + matrix[x_vertex][y_vertex]:
            distance[x_vertex][y_vertex] = distance[i][j] + matrix[x_vertex][y_vertex]
            queue.append((x_vertex,y_vertex))
        

def min_cost_path(n,matrix):
    queue = []
    queue.append((0,0))
    distance = []
    for i in range(n):
        distance.append([100000]*n)
    
    distance[0][0] = matrix[0][0]

    while(len(queue)>0):
        vertex = queue.pop(0)
        i = vertex[0]
        j = vertex[1]
        min_path(matrix,distance,queue,i,j,n,n)
    return distance[n-1][n-1]

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        matrix_arr = [int(x) for x in input().strip(" ").split(" ")]
        matrix = []
        for j in range(n):
            matrix.append(matrix_arr[j*n:(j+1)*n])
        print(min_cost_path(n,matrix))

if __name__ == '__main__':
    main()
    