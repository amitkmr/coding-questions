"""
https://practice.geeksforgeeks.org/problems/largest-sum-subarray-of-size-at-least-k/0

Given an array and a number k, find the largest sum of the subarray containing at least k numbers. It may be assumed that the size of array is at-least k.

Input:​
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the array. Then the following line contains n space separated integers. The last line of the input contains the number k.

Output:
Print the value of the largest sum of the subarray containing at least k numbers.

Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5
1<=k<=n

Example:
Input:
2
4
-4 -2 1 -3
2
6
1 1 1 1 1 1
2

Output:
-1
6

"""


def largest_subarray(arr,n,k):
    i = 0
    j = 0

    arr_sum = 0
    max_sum = min(arr)
    while(i<n-k+1):
        if j<n and (j-i < k or arr_sum + arr[j] > max_sum):
            arr_sum+=arr[j]
            j+=1
            continue
        
        if max_sum < arr_sum:
            max_sum = arr_sum
    
        arr_sum = arr_sum-arr[i]
        i+=1
    

    if arr_sum > max_sum:
        max_sum =arr_sum

    return max_sum


def test():
    a = [-4, -2, 1, -3]
    print(largest_subarray(a,4,2))
    a = [1]*6
    print(largest_subarray(a,6,2))

if __name__ == '__main__':
    # main()
    test()
    