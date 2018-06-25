"""
url:https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle/0

Suppose you have N eggs and you want to determine from which floor in a K-floor building you can drop an egg such that it doesn't break. You have to
determine the minimum number of attempts you need in order find the critical floor in the worst case while using the best strategy.There are few
rules given below.
    * An egg that survives a fall can be used again.
    * A broken egg must be discarded.
    * The effect of a fall is the same for all eggs.
    * If the egg doesn't break at a certain floor, it will not break at any floor below.
    * If the eggs breaks at a certain floor, it will break at any floor above.

For more description on this problem see wiki page

Input:
The first line of input is  T denoting the number of testcases.Then each of the T lines contains two positive integer N and K where 'N' is the number
of eggs and 'K' is number of floor in building.

Output:
For each test case, print a single line containing one integer the minimum number of attempt you need in order find the critical floor.

Constraints:
1<=T<=30
1<=N<=10
1<=K<=50

Example:
Input:
1
2 10

Output:
4
"""

def egg_puzzle(n,k,rem):
    if k < 1:
        return 0
    if n < 1:
        return 1000
    if n == 1:
        rem[n][k] = k
        return rem[n][k]
    
    min_attempts = 100
    for i in range(1,k+1):
        min_attempts = min(min_attempts, max(egg_puzzle(n-1,i-1,rem), egg_puzzle(n,k-i,rem)))
    
    rem[n][k] = 1 + min_attempts
    return rem[n][k]

def main():
    t = int(input())
    for i in range(0,t):
        n_k = input().strip(" ").split(" ")
        n = int(n_k[0])
        k = int(n_k[1])
        rem = []
        for j in range(0,n+1):
            rem.append([-1]*(k+1))
        print(egg_puzzle(n,k,rem))
        print(rem)

if __name__ == '__main__':
    main()
    