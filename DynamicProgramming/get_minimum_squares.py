import math
import unittest

"""
https://practice.geeksforgeeks.org/problems/get-minimum-squares/0
"""


def get_minimum_squares(rem, n):
    if n < 0:
        return 100000

    if n == 0 or n == 1:
        return n

    if rem[n]:
        return rem[n]

    result = 100000
    for i in range(math.floor(math.sqrt(n)), 0, -1):
        result = min(result, get_minimum_squares(rem, n - i * i))

    rem[n] = result

    return result


def min_squares(n):
    rem = [None] * (n + 1)
    return get_minimum_squares(rem, n)


class TestCase(unittest.TestCase):
    def test_get_minimum_squares(self):
        dataT = [(100, 1), (6, 3), (25, 1)]
        for test_case in dataT:
            actual = min_squares(test_case[0])
            self.assertEqual(actual, test_case[1])


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(min_squares(n))


if __name__ == "__main__":
    unittest.main()

