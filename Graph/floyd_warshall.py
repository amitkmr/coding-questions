"""
url : https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0

The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph.

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow . The first line of each test case contains an integer V denoting the size of the adjacency matrix  and in the next line are V*V space separated values of the matrix (graph) .

Output:
For each test case output will be V*V space separated integers where the i-jth integer denote the shortest distance of ith vertex from jth vertex.

Constraints:
1<=T<=20 
1<=V<=20
-1000<=graph[][]<=1000

Example:
Input
2
2
0 25 25 0
3
0 1 43 1 0 6 43 6 0

Output
0 25 25 0 
0 1 7 1 0 6 7 6 0 

0 876 767 905 728 0 325 376 482 428 0 411 352 17 342 0 
0 496 774 11 0 785 529 518 0 

0 876 767 905 728 0 325 376 482 428 0 411 352 17 342 0 
0 496 774 11 0 785 529 518 0 

"""

def print_matrix(distance,v):
    for i in range(v):
        for j in range(v):
            print(distance[i][j],end=" ")
    print()

def floyd_warshall(n,matrix):
    
    distance = []
    for i in range(n):
        distance.append([10000]*n)
    
    for i in range(n):
        for j in range(n):
            # if matrix[i][j] != 0:
            distance[i][j] = matrix[i][j]
            if i==j:
                distance[i][j] = 0
            # else:
                # distance[i][j]

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k]+distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k]+distance[k][j]
            
    print_matrix(distance,n)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        matrix_arr = [int(x) for x in input().strip(" ").split(" ")]
        matrix = []
        for j in range(n):
            matrix.append(matrix_arr[j*n:(j+1)*n])
        floyd_warshall(n,matrix)

if __name__ == '__main__':
    main()
    