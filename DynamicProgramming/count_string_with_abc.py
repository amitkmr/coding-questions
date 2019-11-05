import unittest

"""
https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints/0
"""


def count_strings(n):
    # Can be solved using purely permutation and combination technique
    return int(
        1 + 2 * n + n * (n - 1) + (n * (n - 1)) / 2 + (n * (n - 1) * (n - 2)) / 2
    )


class Test(unittest.TestCase):
    dataT = [(1, 3), (3, 19)]

    def test_count_subsequence(self):
        # true check
        for test_case in self.dataT:
            # print(test_string[0], str(test_string[1]))
            # print(test_string)
            # mem = [None] * (test_case[1] + 1)
            actual = count_strings(test_case[0])
            self.assertEqual(actual, test_case[1])


# def main():
#     t = int(input())
#     for test in range(t):
#         m, n = [int(item) for item in input().strip().split(" ")]
#         arr = [int(item) for item in input().strip().split(" ")]
#         mem = [None] * (n + 1)
#         actual = iter_count(arr, n) % (10 ^ 9 + 7)
#         print(actual)


if __name__ == "__main__":
    unittest.main()
