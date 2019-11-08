import unittest


def max_histogram_area(arr):
    stack = []

    max_area = 0

    # add dummy value to array to push it all the end
    arr.append(0)

    for i in range(len(arr)):
        if len(stack) == 0 or arr[stack[-1]] <= arr[i]:
            stack.append(i)
            continue

        while arr[stack[-1]] > arr[i]:
            last = stack.pop()
            left_index = stack[-1] if len(stack) > 0 else -1
            max_area = max(max_area, (i - left_index - 1) * arr[last])

            if len(stack) == 0:
                break

        stack.append(i)

    return max_area


class TestCase(unittest.TestCase):
    def test_sample(self):
        dataT = [([6, 2, 5, 4, 5, 1, 6], 12), ([6, 3, 4, 2], 9)]
        for item in dataT:
            result = max_histogram_area(item[0])
            self.assertEqual(result, item[1])


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(max_histogram_area(arr))


if __name__ == "__main__":
    unittest.main()
