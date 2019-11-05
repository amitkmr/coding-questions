import unittest

"""
https://practice.geeksforgeeks.org/problems/chicks-in-a-zoo/0

Initially the zoo have a single chick. A chick gives birth to 2 chicks everyday and the life expectancy of a chick is 6 days. Zoo officials want to buy food for chicks so they want to know the number of chicks on a nth day. Help the officials for this task.

Input:
First line of Input contains the number of test cases. Single line of each test case contains the number of days (n).

Output:
Print the required output.

Constraints:
1<=T<=35
1<=N<=35

Example:
Sample Input:
2
3
7
Sample Output:

9
726
"""


def count(mem, n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if mem[n]:
        return mem[n]

    mem[n] = 3 * (count_chick(mem, n - 1) - int(2 * count_chick(mem, n - 6) / 3))
    return mem[n]


def count_chick(n):
    mem = [None] * (max(n, 7) + 1)
    mem[1] = 1
    mem[2] = 3
    mem[3] = 9
    mem[4] = 27
    mem[5] = 81
    mem[6] = 243
    mem[7] = 726

    return count(mem, n)


class Test(unittest.TestCase):
    dataT = [(3, 9), (7, 726)]

    def test_count_subsequence(self):
        # true check
        for test_case in self.dataT:
            # print(test_string[0], str(test_string[1]))
            # print(test_string)
            actual = count_chick(test_case[0])
            self.assertEqual(actual, test_case[1])


def main():
    t = int(input().strip())
    for test in range(t):
        n = int(input().strip())
        actual = count_chick(n)
        print(actual)


if __name__ == "__main__":
    unittest.main()
    # main()
