"""

Given a number N the task is to find an optimal solution to reach N from 0 using 2 operations ie
1. Double the number
2. Add one to the number
Example
Input  : N = 8
Output : 4
0 + 1 = 1, 1 + 1 = 2, 2 * 2 = 4, 4 * 2 = 8

Input  : N = 7
Output : 5
0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.
Output:
For each test case in a new line print an integer denoting the min no of operation to be performed to reach N from 0.
Constraints:
1<=T<=100
1<=N<=10000
Example:
Input:
2
8
7
Input:
4
5

"""
def minimum_operations(n):
    count = 0
    while(n>0):
        if n % 2 == 0:
            n = n/2
        else:
            n = n-1
        count = count +1 
    return count
    
def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        print(minimum_operations(n))

if __name__ == '__main__':
    main()
    