"""
url : https://practice.geeksforgeeks.org/problems/coin-change/0

Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins. The order of coins doesn’t matter. For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

Input:

The first line contains an integer 'T' denoting the total number of test cases. In each test cases, the first line contains an integer 'M' denoting the size of array. The second line contains M space-separated integers A1, A2, ..., AN denoting the elements of the array. The third line contains an integer 'N' denoting the cents.

Output:

Print number of possible ways to make change for N cents.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 300
1 1 ≤ A[i] ≤ 300

Example:

Input:

2
3
1 2 3
4
4
2 5 3 6
10

Output:

4
5

"""


def coin_change(arr, m, r, rem):
    if r < 0:
        return 0
    if m < 0:
        return 0
    if m == 0:
        return 1
    if rem[m][r]:
        return rem[m][r]

    rem[m][r] = coin_change(arr, m - arr[r], r, rem) + coin_change(arr, m, r - 1, rem)
    return rem[m][r]


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input().strip(" "))
        arr = [int(x) for x in input().strip(" ").split(" ")]
        m = int(input())
        rem = []
        for i in range(0, m + 1):
            rem.append([None] * n)
        result = coin_change(arr, m, n - 1, rem)
        print(result)


if __name__ == "__main__":
    main()
