"""
https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k/0

Given an array of positive numbers, the task is to find the number of possible contiguous subarrays having product less than a given number K.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains two integers N & K and the second line contains N space separated array elements.

Output:
For each test case, print the count of required subarrays in new line.

Constraints:
1<=T<=200
1<=N<=105
1<=K<=1015
1<=A[i]<=105

Example:
Input:
2
4 10
1 2 3 4
7 100
1 9 2 8 6 4 3

Output:
7
16

Explanation:

Input : A[]={1, 2,3,4} 
        K = 10
Output : 7
The contiguous subarrays are {1}, {2}, {3}, {4}
{1, 2}, {1, 2, 3} and {2, 3} whose count is 7.

"""


def count(n):
    total = 0
    for i in range(1,n+1):
        total = total+(n-i+1)
    return total
    
def count_subset(arr,n,k):
    i = 0
    j = 0
    
    multi = 1
    subset = 0
    sep = -1
    while(j<n):
        if multi*arr[j] < k and j<n-1:
            multi*=arr[j]
            j+=1
            continue
        subset+=count(j-i)-count(sep-i+1)
        multi*=arr[j]
        while(multi>= k and i<=j):
            multi//=arr[i]
            i+=1
        sep = j-1
        j+=1
        
    subset+=count(j-i)-count(sep-i+1)
    
    print(subset)

def main():
    t = int(input())
    for i in range(t):
        n,k = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        count_subset(arr,n,k)


if __name__ == '__main__':
    main()