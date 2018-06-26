"""
Given an array having both positive an negative integers . Your task is to complete the function maxLen which returns the length of maximum subarray with 0 sum . The function takes two arguments an array A and n where n is the size of the array A . 

Input:
The first line of input contains an element T denoting the No of test cases. Then T test cases follow. Each test case consist of 2 lines. The first line of each test case contains a number denoting the size of the array A. Then in the next line are space separated values of the array A .

Output:
For each test case output will be the length of the largest subarray which has sum 0 .

Constraints:
1<=T<=100
1<=N<=100
-1000<=A[]<=1000

Example:
Input
1
8
15  -2  2  -8  1  7  10 23

Output
5

"""

# Contributed by: Harshit Sidhwa

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    #Code here
    index_arr = [0]*(n)
    max_sum = 0
    for i in range(0,len(arr)):
        arr_sum = 0
        for j in range(i,len(arr)):
            arr_sum = arr_sum + arr[j]
            if arr_sum == 0:
                index_arr[i] = j-i+1
    return max(index_arr)

if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))