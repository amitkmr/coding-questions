"""
url : https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0

You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item, In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
 

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines. The first line consists of N the number of items. The second line consists of W, the maximum capacity of the knapsack. In the next  line are N space separated positive integers denoting the values of the N items and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.
 

Output:

Print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.
 

Constraints:

1≤T≤100

1≤N≤100

1≤W≤100

1≤wt[i]≤100

1≤v[i]≤100


Example:

Input:
1
3
4
1 2 3
4 5 1
Output:
3
"""

def zero_1_knapsack(weight,values,w,r,rem):
    if w < 0:
        return -10000
    if w == 0 or r < 0:
        return 0
    if rem[w][r] !=-1:
        return rem[w][r]

    rem[w][r] =  max(values[r]+zero_1_knapsack(weight,values,w-weight[r],r-1,rem),zero_1_knapsack(weight,values,w,r-1,rem))
    return rem[w][r]
        
    

def main():
   t = int(input())
   for i in range(0,t):
       n = int(input())
       w = int(input())
       values = [int(x) for x in input().strip(" ").split(" ")]
       weight = [int(x) for x in input().strip(" ").split(" ")]
       rem = []
       for i in range(0,w+1):
           rem.append([-1]*len(weight))
       print(zero_1_knapsack(weight,values,w,len(weight)-1,rem))

if __name__ == '__main__':
    main()
    