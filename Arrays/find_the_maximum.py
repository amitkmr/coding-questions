"""
https://practice.geeksforgeeks.org/problems/find-the-maximum-sum/0

Given an array of n elements.Find the maximum sum when the array elements will be arranged in such way. Multiply the elements of each pair and add to get maximum Sum. Sum could be larger so take mod with 10^9+7.

Example1: 
Input:  n=7
        -1,9,4,5,-4,-7,0
Output: 77
So to get the maximum sum,the arrangement will be {-7,-4},{-1,0},{9,5} and {4}.So the answer is (-7*(-4))+((-1)*0)+(9*5)+(4) ={77}.

Example2:
Input:  n=3
        -1,0,1
Output: 1
So to get the maximum sum,the arrangement will be {-1,0} and {1}.So the answer is ((-1)*0)+(1)={1}.
Input:
The first line consists of an integer T i.e number of test cases. The first line of each test case consists of an integer n.The next line consists of n spaced integers(positive or negative).

Output:
Print the maximum sum % 10^9+7.

Constraints: 
1<=T<=100
1<=n,a[i]<=10000

Example:
Input:
2
3
8 7 9
6
-1 9 4 5 -4 7

Output:
79
87

"""

def max_sum(arr,n):
    arr = sorted(arr)

    total = 0

    r = n-2
    while(r>=0):
        if arr[r]>0 and arr[r+1] > 0:
            total+=arr[r]*arr[r+1]
        else:
            break
        r-=2
    if r == -2:
        return total
    if r == -1:
        return total + arr[0]
    
    l = 0
    # print(arr)
    while(l<n-1):
        # print("total : "+str(total))
        if arr[l] < 0 and arr[l+1] < 0:
            total+=arr[l]*arr[l+1]
        else:
            break
        l+=2        

    if l==n-1:
        return total + arr[n-1]
    if l==n:
        return total
    
    if n%2 == 0:
        if r<l:
            return total
        if l==r:
            return total + arr[l]*arr[l+1]
    else:
        total = total + arr[l]
    return total

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        result = max_sum(arr,n)
        large = (10**9+7)
        if result > large:
            print(result%large)
        else:
            print(result)

if __name__ == '__main__':
    main()