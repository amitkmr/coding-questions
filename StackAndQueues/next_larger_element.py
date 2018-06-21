"""
url : https://practice.geeksforgeeks.org/problems/next-larger-element/0

Given an array A [ ] having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A[ ].
 
Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Constraints:
1<=T<=200
1<=N<=1000
1<=A[i]<=1000

Example:
Input
1
4
1 3 2 4 

Output
3 4 4 -1

Explanation
In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? since it doesn't exist hence -1.

"""

def next_larger_element(arr,n):
    stack = []
    result = [-1]*n
    for i in range(0,n):
        while(len(stack)>0 and arr[stack[-1]]<arr[i]):
            pop_index = stack.pop()
            result[pop_index] = arr[i]
        stack.append(i) 
    for item in result:
        print(item, end=" ")
    print()

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip().split(" ")];
        next_larger_element(arr,n)

if __name__ == '__main__':
    main()
    