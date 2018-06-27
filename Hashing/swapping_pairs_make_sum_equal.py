"""
Given two arrays of integers, write a program to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

Input:
First line of input contains a single integer T which denotes the number of test cases. T test cases follows. First line of each test case contains two space separated integers N and M. Second line of each test case contains N space separated integers denoting the elements of first array. Third line of each test case contains M space separated integers denoting the elements of second array.

Output:
For each test case, print 1 if there exists any such pair otherwise print -1.

Constraints:
1<=T<=100
1<=N<=10000
1<=M<=10000

Example:
Input:
2
6 4
4 1 2 1 1 2
3 6 3 3
4 4
5 7 4 6
1 2 3 8
Output:
1
1
"""

def swapping_pair(arr1,arr2):
    sum1 = sum(arr1)
    sum2 = sum(arr2)

    diff  = abs(sum1 - sum2)
    if diff%2 !=0:
        return -1
    item = int(diff/2)

    for item1 in arr1:
        for item2 in arr2:
            if abs(item1-item2) == item:
                return 1
    
    return -1

def main():
    t = int(input())
    for i in range(0,t):
        numbers = input().strip(" ").split(" ")
        n = int(numbers[0])
        m = int(numbers[1])
        arr1 = [int(x) for x in input().strip(" ").split(" ")]
        arr2 = [int(x) for x in input().strip(" ").split(" ")]
        print(swapping_pair(arr1,arr2))
if __name__ == '__main__':
    main()