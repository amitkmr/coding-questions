import unittest


def immediate_largest_number(number):
    digits = [int(digit) for digit in str(number)]

    if len(digits) == 1:
        return 0

    break_idx = None

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break_idx = i
            break

    if not break_idx:
        return 0

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] > digits[break_idx]:
            digits[i], digits[break_idx] = digits[break_idx], digits[i]
            break

    return int(
        "".join(
            [
                str(digit)
                for digit in digits[: break_idx + 1] + sorted(digits[break_idx + 1 :])
            ]
        )
    )


class TestCase(unittest.TestCase):
    def test_largest_number(self):
        dataT = [
            (1234, 1243),
            (4321, 0),
            (10001, 10010),
            (218765, 251678),
            (534976, 536479),
        ]

        for number, expected in dataT:
            result = immediate_largest_number(number)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
