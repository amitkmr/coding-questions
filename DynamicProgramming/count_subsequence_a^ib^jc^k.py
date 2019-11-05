"""
Given a string s, the task is to count number of subsequences of the form aibjck, where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.


Examples:

Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc
abcc, abc and abc


Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains a string s.

Output:
For each test case in a new line print the required output.

"""
import unittest


def count_subsequence(prev, string):
    if len(string) == 0:
        if prev == "c":
            return 1
        else:
            return 0
    if prev == "":
        if string[0] == "a":
            return count_subsequence("", string[1:]) + count_subsequence(
                string[0], string[1:]
            )
        else:
            return count_subsequence("", string[1:])

    if prev == "a":
        if string[0] == "a":
            return 2 * count_subsequence(prev, string[1:])
        elif string[0] == "b":
            return count_subsequence(prev, string[1:]) + count_subsequence(
                string[0], string[1:]
            )
        else:
            return count_subsequence(prev, string[1:])

    if prev == "b":
        if string[0] == "b":
            return 2 * count_subsequence(prev, string[1:])
        elif string[0] == "c":
            return count_subsequence(prev, string[1:]) + count_subsequence(
                string[0], string[1:]
            )
        else:
            return count_subsequence(prev, string[1:])

    if prev == "c":
        if string[0] == "c":
            return 2 * count_subsequence(prev, string[1:])
        else:
            return count_subsequence(prev, string[1:])


def count(string):
    return count_subsequence("", string)


def main():
    t = int(input())
    for _ in range(t):
        string = input()
        print(count(string))


class Test(unittest.TestCase):
    dataT = [("abc", 1), ("abbc", 3), ("abcabc", 7)]

    def test_count_subsequence(self):
        # true check
        for test_string in self.dataT:
            # print(test_string[0], str(test_string[1]))
            # print(test_string)
            actual = count(test_string[0])
            self.assertEqual(actual, test_string[1])


if __name__ == "__main__":
    unittest.main()
    # main()
