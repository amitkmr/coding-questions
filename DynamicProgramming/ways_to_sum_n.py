import unittest

"""
https://practice.geeksforgeeks.org/problems/ways-to-sum-to-n/0
"""


def rec_count(mem, arr, n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if mem[n]:
        return mem[n]

    result = 0
    for item in arr:
        if item != 0:
            result += rec_count(mem, arr, n - item)
    mem[n] = result

    return mem[n]


def iter_count(arr, n):
    count = [0] * (n + 1)
    count[0] = 1

    for j in range(n + 1):
        for item in arr:
            if j >= item:
                count[j] += count[j - item]

    return count[n]


class Test(unittest.TestCase):
    dataT = [([1, 5, 6], 7, 6)]

    def test_count_subsequence(self):
        # true check
        for test_case in self.dataT:
            # print(test_string[0], str(test_string[1]))
            # print(test_string)
            mem = [None] * (test_case[1] + 1)
            actual = count(mem, test_case[0], test_case[1])
            print(mem)
            self.assertEqual(actual, test_case[2])


def main():
    t = int(input())
    for test in range(t):
        m, n = [int(item) for item in input().strip().split(" ")]
        arr = [int(item) for item in input().strip().split(" ")]
        mem = [None] * (n + 1)
        actual = iter_count(arr, n) % (10 ^ 9 + 7)
        print(actual)


if __name__ == "__main__":
    main()
