"""
url : https://practice.geeksforgeeks.org/problems/maximize-toys/0
Given an array consisting cost of toys. Given an integer K depicting the amount with you. Maximise the number of toys you can have with K amount.

Input:

The first line contains an integer T, depicting total number of test cases.
Then following T lines contains an integer N depicting the number of toys and an integer K depicting the value of K.
Next line is followed by the cost of toys.

Output:

Print the maximum toys in separate line.

Constraints:

1 <= T <= 30
1 <= N <= 1000
1 <= K <= 10000
1 <= A[i] <= 10000

Example:

Input
1
7 50
1 12 5 111 200 1000 10
Output
4
"""

def maximum_toys(arr,n,k):
    arr = sorted(arr)
    index = 0
    count = 0
    while(k>0 and index < n):
        if k - arr[index] >= 0:
            k = k - arr[index]
            count = count + 1
            index = index + 1
        else:
            break
    print(count)
        

def main():
    t = int(input().strip())
    for i in range(0,t):
        numbers = input().strip().split(" ")
        n = int(numbers[0])
        k = int(numbers[1])

        arr = [int(x) for x in input().strip().split(" ")]
        maximum_toys(arr,n,k)

if __name__ == '__main__':
    main()