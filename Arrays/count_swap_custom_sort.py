import unittest


def count_sort_count(arr):
    i = 0
    j = len(arr) - 1

    count = 0
    while (i < j):
        while arr[i] % 2 == 0:
            i += 1

        while arr[j] % 2 == 1:
            j -= 1

        i += 1
        j -= 1
        count += 1

    return count


class TestCase(unittest.TestCase):
    def test_custom_sort_count(self):
        arr = [2, 3, 4, 5, 6, 7, 1, 5, 6]
        result = count_sort_count(arr)
        print(result)


if __name__ == "__main__":
    unittest.main()