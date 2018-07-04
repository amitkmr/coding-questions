"""
https://practice.geeksforgeeks.org/problems/circular-tour/1

Suppose there is a circle. There are n petrol pumps on that circle. You will be given two sets of data.

1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Your task is to complete the function tour which returns an integer denoting the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity).

Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Input
The first line of input will be the no of test cases . Then T test cases follow . Each Test case contains 2 lines . The first line will contain an integer N denoting the no of petrol pumps and in the next line are N space separated values petrol and distance denoting the amount of petrol every petrol pump has and the distance to next petrol pump respectively .

Output
The output of each test case will be the index of the the first point from where a truck will be able to complete the circle otherwise -1 .

Constraints:
1<=T<=100
1<=N<=50
1<=petrol,distance<=100

Example (To be used only for expected output)
Input
1
4
4 6 6 5 7 3 4 5
Output
1
"""


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
#Your task isto complete this function
#Your function should return the starting point
def tour(lis, n):
    l = 0
    r = 0
    sum = 0
    count = 0
    while(count<n):
        sum = sum + (lis[r][0] - lis[r][1])
        count = count + 1
        while(sum<0):
            sum = sum-(lis[l][0] - lis[l][1])
            count = count -1
            l = l + 1
            if l == n:
                return -1
        r = r + 1
        if r == n:
            r = 0
    return l

t = int(input())
for i in range(t):
    n = int(input())
    arr=list(map(int, input().strip().split()))
    lis=[]
    for i in range(1, 2*n, 2):
        lis.append([ arr[i-1], arr[i] ])
    #print n, arr
    print(tour(lis, n))
# Contributed by: Harshit Sidhwa