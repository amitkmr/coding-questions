"""
https://practice.geeksforgeeks.org/problems/unsorted-array/0

Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.

Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated array elements.

Output:
For each test case, in a new line print the required element. If no such element present in array then print -1.

Constraints:
1<=T<=100
3<=N<=106
1<=A[i]<=106

Example:
Input:
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9

Output:
5
-1
7

"""
def find_left_side_smaller(arr,n):
    if len(arr) == 0:
        return -1
    left_max = arr[0]
    left = []
    for i in range(1,n-1):
        if arr[i]>=left_max:
            left.append(i)
            left_max = arr[i]
    
    right_min = arr[n-1]
    right = []
    for i in range(1,n-1):
        if arr[n-1-i] <= right_min:
            right.append(n-1-i)
            right_min = arr[n-1-i]
    
    for i in left:
        if i in right:
            return arr[i]
    return -1
        
def main():
    t = int(input())
    for i in range(t):
        n = int(input().strip(" "))
        arr = [int(x) for x in input().strip(" ").split(" ")]
        print(find_left_side_smaller(arr,n))

if __name__ == '__main__':
    main()
    