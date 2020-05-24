"""
problem statement: 
"""

import unittest


def find_triplet(arr):
    arr = sorted(arr)  # nlogn step
    l = 0
    r = len(arr) - 1


class TestCase(unittest.TestCase):
    def test_triplet_sum(self):
        dataT = [([0, -1, 2, -3, 1], (-1, 0, 1))]
        for test in dataT:
            result = find_triplet(test[0])
            assert result == test[1]


if __name__ == "__main__":
    unittest.main()
