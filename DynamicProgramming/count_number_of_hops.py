"""
url:https://practice.geeksforgeeks.org/problems/count-number-of-hops/0

Frog steps either 1, 2 or 3 steps to go to top. In how many ways it reaches the top?

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N. Where is the number of steps it has to hop.

Output:

Print the number of ways.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 50

Example:

Input:
2
1
5

Output:
1
13

"""

def number_of_hops(n,rem):
    if n<0:
        return 0
    if n==0:
        return 1
    
    if rem[n]!= -1:
        return rem[n]
    
    steps = [1,2,3]
    hops = 0
    for step in steps:
        hops = hops + number_of_hops(n-step,rem)
    rem[n] = hops
    return hops

def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        rem = [-1]*(n+1)
        print(number_of_hops(n,rem))
if __name__ == '__main__':
    main()
    