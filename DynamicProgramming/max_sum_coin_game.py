import unittest


def max_sum(arr, i, j):
    if i == j:
        return arr[i]

    if i + 1 == j:
        return max(arr[i], arr[j])

    return max(
        arr[i] + min(max_sum(arr, i + 2, j), max_sum(arr, i + 1, j - 1)),
        arr[j] + min(max_sum(arr, i, j - 2), max_sum(arr, i + 1, j - 1)),
    )


class TestCase(unittest.TestCase):
    def test_game(self):
        dataT = [([8, 15, 3, 7], 22), ([2, 2, 2, 2], 4), ([20, 30, 2, 2, 2, 10], 42)]

        for item in dataT:
            result = max_sum(item[0], 0, len(item[0]) - 1)
            self.assertEqual(result, item[1])


if __name__ == "__main__":
    unittest.main()
