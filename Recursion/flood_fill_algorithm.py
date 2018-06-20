"""
https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0

Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

                      {{1, 1, 1, 1, 1, 1, 1, 1},
                      {1, 1, 1, 1, 1, 1, 0, 0},
                      {1, 0, 0, 1, 1, 0, 1, 1},
                      {1, 2, 2, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 0, 1, 0},
                      {1, 1, 1, 2, 2, 2, 2, 0},
                      {1, 1, 1, 1, 1, 2, 1, 1},
                      {1, 1, 1, 1, 1, 2, 2, 1},
                      };

                        x=4, y=4, color=3 

                               {{1, 1, 1, 1, 1, 1, 1, 1},
                     {1, 1, 1, 1, 1, 1, 0, 0},
                     {1, 0, 0, 1, 1, 0, 1, 1}, 
                     {1, 3, 3, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 0, 1, 0},
                     {1, 1, 1, 3, 3, 3, 3, 0},
                     {1, 1, 1, 1, 1, 3, 1, 1},
                     {1, 1, 1, 1, 1, 3, 3, 1}, };


Note: Use zero based indexing.


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains Two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix. Then in the next line are three values x, y and K.

Output:
For each test case print the space separated values of the new matrix.

Constraints:
1<=T<=100
1<=M[][]<=100

Example:
Input:
3
3 4
0 1 1 0 1 1 1 1 0 1 2 3
0 1 5
2 2
1 1 1 1
0 1 8
4 4 
1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4
0 2 9

Output:
0 5 5 0 5 5 5 5 0 5 2 3
8 8 8 8
1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4

"""


def array_to_matrix(arr,n,m):
    matrix = []
    arr_index = 0
    for j in range(0,n):
          row = []
          for k in range(0,m):
                row.append(arr[arr_index])
                arr_index = arr_index + 1
          matrix.append(row)
    return matrix

def fill_k(matrix,n,m,x,y,c,k):
      if x<0 or y<0 or x>= n or y >= m:
            return
      if matrix[x][y] != c:
            return
      matrix[x][y] = k
      # recursive call
      fill_k(matrix,n,m,x+1,y,c,k);
      fill_k(matrix,n,m,x,y+1,c,k);
      fill_k(matrix,n,m,x-1,y,c,k);
      fill_k(matrix,n,m,x,y-1,c,k);
      

def flood_fill_algorithm(matrix,n,m,x,y,k):
      fill_k(matrix,n,m,x,y,matrix[x][y],k)

def printMatrix(matrix):
      for row in matrix:
            for item in row:
                print(item, end=" ")
      print()


def main():
      t = int(input())

      for i in range(0,t):
            numbers = input().strip().split(" ")
            n = int(numbers[0])
            m = int(numbers[1])

            matrix_arr = [int(x) for x in input().strip().split(" ")]
            x_y_k = input().strip().split(" ")
            x = int(x_y_k[0])
            y = int(x_y_k[1])
            k = int(x_y_k[2])
            matrix = array_to_matrix(matrix_arr,n,m)
            flood_fill_algorithm(matrix,n,m,x,y,k)
            printMatrix(matrix)

if __name__ == '__main__':
    main()
    
