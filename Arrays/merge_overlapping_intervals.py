import unittest


def sort_key(interval):
    return interval[0]


def merge(arr):
    arr = sorted(arr, key=sort_key)

    result = []

    last_start = None
    last_finish = None
    for start, finish in arr:
        if not last_start:
            last_start, last_finish = start, finish
            continue

        if start <= last_finish:
            last_finish = max(finish, last_finish)
        else:
            result.append((last_start, last_finish))
            last_start, last_finish = start, finish

    result.append((last_start, last_finish))

    return result


class TestCase(unittest.TestCase):
    def test_merge(self):
        dataT = [[(6, 8), (1, 9), (2, 4), (4, 7)], [(1, 3), (2, 4), (5, 7), (6, 8)]]

        for test in dataT:
            result = merge(test)
            print(result)


if __name__ == "__main__":
    unittest.main()
