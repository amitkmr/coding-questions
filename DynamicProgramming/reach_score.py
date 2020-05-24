import unittest

"""
https://practice.geeksforgeeks.org/problems/reach-a-given-score/0
"""


def reach_score(rem, arr, n):
    if n == 0:
        return 1

    if n < 0 or len(arr) == 0:
        return 0

    if rem[n]:
        return rem[n]

    return reach_score(rem, arr[:-1], n) + reach_score(rem, arr, n - arr[-1])


def reach(n):
    arr = [3, 5, 10]
    rem = [None] * (n + 1)
    return reach_score(rem, arr, n)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(reach(n))


class TestCase(unittest.TestCase):
    def test_reach_score(self):
        dataT = [(8, 1), (20, 4), (13, 2)]

        for test_case in dataT:
            actual = reach(test_case[0])
            self.assertEqual(actual, test_case[1])


if __name__ == "__main__":
    unittest.main()
