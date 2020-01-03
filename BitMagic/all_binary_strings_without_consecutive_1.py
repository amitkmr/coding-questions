import unittest


def next_string(string, i, n):
    if i == n:
        return [string]

    if len(string) == 0 or string[-1] == "" or string[-1] == "0":
        return next_string(string + "0", i + 1, n) + next_string(
            string + "1", i + 1, n)
    else:
        return next_string(string + "0", i + 1, n)


class TestCase(unittest.TestCase):
    def test_print_strings(self):
        dataT = [3, 4, 5]

        for item in dataT:
            results = next_string("", 0, item)
            print(results)


if __name__ == "__main__":
    unittest.main()