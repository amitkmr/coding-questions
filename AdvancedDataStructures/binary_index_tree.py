import unittest


class BinaryIndexTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (len(arr) + 1)
        self.construct_tree(arr=arr)

    def get_range_sum(self, ql, qr):
        return self.sum(0, self.arr_len - 1, 0, ql, qr)

    def sum(self, l, r, index, ql, qr):
        if qr < l or ql > r:
            return 0
        if ql <= l and qr >= r:
            return self.tree[index]

        mid = (l + r) // 2

        return self.sum(l, mid, 2 * index + 1, ql, qr) + self.sum(
            mid + 1, r, 2 * index + 2, ql, qr
        )

    def update(self, key_index, key):
        index = key_index + 1
        difference = key - self.arr[key_index]

        while index > 0:
            self.tree[index] += difference
            index = index & (index - 1)

        self.tree[index] += difference

    def construct_tree(self, arr):
        for i in range(len(arr)):
            index = i + 1
            child_sum = arr[i]
            while index > 0:
                self.tree[index] += child_sum
                index = index & (index - 1)

            self.tree[index] += child_sum


class TestCase(unittest.TestCase):
    def test_segment_tree(self):
        arr = [1, 3, 5, 7, 9, 11]
        tree = BinaryIndexTree(arr=arr)
        print(tree.tree)
        tree.update(2, 10)
        print(tree.tree)

        print(tree.get_range_sum(0, 2))
        # print(tree.get_range_sum(4, 5))
        # tree.udpate(5, 19)
        # print(tree.get_range_sum(4, 5))
        # tree.udpate(2, 10)
        # print(tree.get_range_sum(0, 2))


if __name__ == "__main__":
    unittest.main()
