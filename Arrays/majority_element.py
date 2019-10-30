import unittest

# Check if an array has a majority element
# Given an array, the task is to find if the input array contains a majority element or not. An element is

# Examples:

# Input : arr[] = {2, 3, 9, 2, 2}
# Output : Yes
# A majority element 2 is present in arr[]

# Input  : arr[] = {1, 8, 9, 2, 5}
# Output : No


def majority_algorithm(arr):
    maj_index = 0
    count = 1

    for index in range(1, len(arr)):
        if arr[index] == arr[maj_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = index
            count = 1

    # check if maj_index has is element with more than n/2 count

    count = 0

    for item in arr:
        if arr[maj_index] == item:
            count += 1

    if count > len(arr) // 2:
        return arr[maj_index]
    else:
        return "No"


class Test(unittest.TestCase):
    def test_majority_algorithm(self):
        data = [([2, 3, 9, 2, 2], 2), ([1, 8, 9, 2, 5], "No")]
        for test in data:
            self.assertEqual(majority_algorithm(test[0]), test[1])


if __name__ == "__main__":
    unittest.main()
