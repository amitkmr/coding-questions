"""

Given two arrays, A and B, of equal size n, the task is to find the minimum value  of A[0] * B[0] + A[1] * B[1] +...+ A[n-1] * B[n-1], where
shuffling of elements of arrays A and B is allowed.

Examples:
Input : A[] = {3, 1, 1} and B[] = {6, 5, 4}.
Output : 23 Minimum value of S = 1*6 + 1*5 + 3*4 = 23.
Input : A[] = { 6, 1, 9, 5, 4 } and B[] = { 3, 4, 8, 2, 4 }
Output : 80. Minimum value of S = 1*8 + 4*4 + 5*4 + 6*3 + 9*2 = 80.

Input:
The first line of input contains an integer denoting the no of test cases. Then T test cases follow. Each test case contains three lines. The first
line of input contains an integer N denoting the size of the arrays. In the second line are N space separated values of the array A[], and in
the last line are N space separated values of the array B[].
Output:
For each test case in a new line print the required result.
Constraints:
1<=T<=100
1<=N<=50
1<=A[]<=20
Example:
Input:
2
3
3 1 1
6 5 4
5
6 1 9 5 4
3 4 8 2 4
Output:
23
80

"""
def multiply(n,arr1,arr2):
    product = 0
    for i in range(0,n):
        product = product + arr1[i]*arr2[i]
    return product

def minimize_product(n,arr1,arr2):
    return multiply(n,sorted(arr1),sorted(arr2,reverse=True))

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr1 = [int(x) for x in input().strip().split(" ")]
        arr2 = [int(x) for x in input().strip().split(" ")]
        print(minimize_product(n,arr1,arr2))
if __name__ == '__main__':
    main()
    