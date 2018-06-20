"""
https://practice.geeksforgeeks.org/problems/number-of-paths/0

he problem is to count all the possible paths from top left to bottom right of a  MxN matrix with the constraints that from each cell you can either move to right or down.

Input:
The first line of input contains an integer T, denoting the number of test cases.
The first line of each test case is M and N, M is number of rows and N is number of columns.

Output:
For each test case, print the number of paths.

Constraints:

1 ≤ T ≤ 30
1 ≤ M,N ≤ 10

Example:
Input
2
3 3
2 8
Output
6
8

"""

def number_of_paths(x,y,n,m):
    if x >= n or y >= m:
        return 0
    if x == n-1 and y == m-1:
        return 1
    return number_of_paths(x+1,y,n,m) + number_of_paths(x,y+1,n,m)   

def main():
    t = int(input())
    for i in range(0,t):
        numbers = input().strip().split(" ")
        n = int(numbers[0])
        m = int(numbers[1])
        print(number_of_paths(0,0,n,m))

if __name__ == '__main__':
    main()
    