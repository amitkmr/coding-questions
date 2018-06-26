"""
url : https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Input:The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements of the set.
Output: Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets is equal, else print NO.
Constraints: 

1 <= T<= 100
1 <= N<= 100
0 <= arr[i]<= 1000

                   
Example:

Input:
2
4
1 5 11 5
3
1 3 5 

Output:

YES
NO

"""
def subtract(arr1,arr2):
    result = []
    for item in arr1:
        if item not in arr2:
            result.append(item)
    return result
    
def subset(arr,r,sub,s_sum,rem):
    if s_sum == 0:
        return sub
    if r<0 or s_sum <0 :
        return[]
        
    if rem[s_sum][r]!=-1:
        return rem[s_sum][r]
    
    result = subset(arr,r-1,sub+[arr[r]],s_sum-arr[r],rem)
    if len(result)==0:
        rem[s_sum][r] = subset(arr,r-1,sub,s_sum,rem)
        return rem[s_sum][r]
    else:
        rem[s_sum][r] = result
        return result
      
def subset_sum(arr,n):
    if sum(arr)%2 !=0:
        return 'NO'
    s_sum = int(sum(arr)/2)
    sub = []
    rem = []
    for i in range(0,s_sum+1):
        rem.append([-1]*(n))
    result1 = subset(arr,n-1,sub,s_sum,rem)
    if len(result1) == 0:
        return 'NO'
    
    arr.remove(result1[0])
    sub = []
    rem = []
    for i in range(0,s_sum+1):
        rem.append([-1]*(len(arr)))
    result2 = subset(arr,len(arr)-1,sub,s_sum,rem)
    if len(result2) == 0:
        return 'NO'
    else:
        return 'YES'

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip(" ").split(" ")]
        print(subset_sum(arr,n))

if __name__ == '__main__':
    main()