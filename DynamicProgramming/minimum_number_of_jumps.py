"""
url : 

Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Input: 
The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains a number n denoting the size of the array.
Next line contains the sequence of integers a1, a2, ..., an.

Output:
Each seperate line showing the minimum number of jumps. If answer is not possible print -1.

Constraints:
1 ≤ T ≤ 40
1 ≤ N ≤ 100
0<=a[N]<=100

Example:

Input:

1
11
1 3 5 8 9 2 6 7 6 8 9

"""

def minimum_jumps(arr,i,rem):
    if i < 0:
        return 1000
    if i == 0:
        return 0
    if rem[i] != -1:
        return rem[i]
    
    min_jumps = 1000
    j = i-1
    while(j>=0):
        if arr[j] >= i-j:
            min_jumps = min(min_jumps, 1 + minimum_jumps(arr,j,rem))
        j = j - 1
    rem[i] = min_jumps
    return rem[i]

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input().strip(" "))
        arr = [int(x) for x in input().strip(" ").split(" ")]
        rem = [-1] * n
        result = minimum_jumps(arr,n-1,rem)
        if result == 1000:
            print(-1)
        else:
            print(result)
        
if __name__ == '__main__':
    main()