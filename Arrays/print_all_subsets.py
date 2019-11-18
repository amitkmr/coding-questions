import unittest
from copy import copy


def subsets(arr):
    if len(arr) == 0:
        return [[]]

    item = arr[0]
    sets = subsets(arr[1:])
    item_sets = []

    for s in sets:
        new_set = s[:]
        new_set.append(item)
        item_sets.append(new_set)
    return sets + item_sets


class TestCase(unittest.TestCase):
    def test_subsets(self):
        dataT = [[1, 2, 3]]

        for data in dataT:
            result = subsets(data)
            print(result)


if __name__ == "__main__":
    unittest.main()
