import unittest
from collections import deque


def largest_k_window(arr, k):
    q = deque()

    result = []

    for i in range(len(arr)):
        if len(q) == 0:
            q.append(i)
            continue

        while len(q) != 0 and arr[i] > arr[q[-1]]:
            q.pop()
        q.append(i)

        if i - k == q[0]:
            q.popleft()

        if i >= k - 1:
            result.append(arr[q[0]])
    return result


class TestCase(unittest.TestCase):
    def test_largest_in_k_window(self):
        dataT = [
            ([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4),
            ([12, 1, 78, 90, 57, 89, 56], 3),
            ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3),
        ]

        for item in dataT:
            result = largest_k_window(item[0], item[1])
            print(result)


if __name__ == "__main__":
    unittest.main()
