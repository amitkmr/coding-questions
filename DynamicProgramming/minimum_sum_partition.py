"""
url : https://practice.geeksforgeeks.org/problems/minimum-sum-partition/0
Given an array, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.

Input:
The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.


Output:
In each seperate line print minimum absolute difference.


Constraints:
1<=T<=30
1<=N<=50
1<=A[I]<=50


Example:
Input:
2
4
1 6 5 11
4
36 7 46 40

Output : 
1
23

Explaination :
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11},       sum of Subset2 = 11
"""

def subset(arr,r,s_sum,rem):
    if s_sum == 0:
        return True
    if r<0 or s_sum <0 :
        return False
        
    if rem[s_sum][r]!=-1:
        return rem[s_sum][r]

    rem[s_sum][r]  = subset(arr,r-1,s_sum-arr[r],rem) or subset(arr,r-1,s_sum,rem)
    return rem[s_sum][r]


def subset_sum(arr,n):
    arr_sum = sum(arr)
    a_sum = int(arr_sum/2)
    b_sum = arr_sum - a_sum

    rem = []
    for i in range(0,arr_sum):
        rem.append([-1]*(n))

    while(a_sum>0 and b_sum < arr_sum):
        if subset(arr,n-1,a_sum,rem) and subset(arr,n-1,b_sum,rem):
            return b_sum - a_sum
        else:
            a_sum = a_sum - 1
            b_sum = b_sum + 1
    return b_sum - a_sum

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip(" ").split(" ")]
        print(subset_sum(arr,n))

if __name__ == '__main__':
    main()