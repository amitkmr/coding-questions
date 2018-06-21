"""
url : https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0

Given a value N, if we want to make change for N Rs, and we have infinite supply of each of the denominations in Indian currency, i.e., we have
infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, Find the minimum number of coins and/or notes needed to make the
change.

Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case consist of an Integer value N denoting the amount to get change for.

Output:

Print all the possible denominations needed to make the change in a separate line.

Constraints:

1 <= T <= 30
1 <= N <= 2000

Example:

Input
1
43
Output
20 20 2 1
"""

def minimum_coins(n,coins):
    index = len(coins) - 1
    while(n>0 and index >= 0):
        if n - coins[index] >= 0:
            n = n - coins[index]
            print(coins[index], end=" ")
        else:
            index = index - 1
    print()

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    t = int(input())
    for i in range(0,t):
        n = int(input())
        minimum_coins(n,coins)


if __name__ == '__main__':
    main()