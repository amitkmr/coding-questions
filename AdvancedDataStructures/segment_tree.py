import unittest


class SegmentTree:
    def __init__(self, arr):
        self.arr_len = len(arr)
        self.tree = [None] * (2 * len(arr) + 1)
        self.construct_tree(arr, 0, len(arr) - 1, 0)

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

    def update_key(self, key_index, key, l, r, index):
        if l == r and l == key_index:
            difference = key - self.tree[index]
            self.tree[index] = key
            return difference

        mid = (l + r) // 2

        if key_index <= mid:
            difference = self.update_key(key_index, key, l, mid, 2 * index + 1)
        else:
            difference = self.update_key(key_index, key, mid + 1, r, 2 * index + 2)

        self.tree[index] += difference
        return difference

    def udpate(self, key_index, key):
        self.update_key(key_index, key, 0, self.arr_len - 1, 0)

    def construct_tree(self, arr, l, r, index):
        if l == r:
            self.tree[index] = arr[l]
            return self.tree[index]

        mid = (l + r) // 2

        self.tree[index] = self.construct_tree(
            arr, l, mid, 2 * index + 1
        ) + self.construct_tree(arr, mid + 1, r, 2 * index + 2)

        return self.tree[index]


class TestCase(unittest.TestCase):
    def test_segment_tree(self):
        arr = [1, 3, 5, 7, 9, 11]
        tree = SegmentTree(arr=arr)

        print(tree.get_range_sum(0, 2))
        print(tree.get_range_sum(4, 5))
        tree.udpate(5, 19)
        print(tree.get_range_sum(4, 5))
        tree.udpate(2, 10)
        print(tree.get_range_sum(0, 2))


if __name__ == "__main__":
    unittest.main()
