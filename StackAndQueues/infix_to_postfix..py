import unittest


def priority(char):
    if char == "+" or char == "-":
        return 1
    if char == "*" or char == "/":
        return 2
    if char == "^":
        return 3
    return 0


def infix_to_postfix(string):

    stack = []
    result = ""
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
            continue
        if string[i] == ")":
            while len(stack) > 0:
                item = stack.pop()
                if item == "(":
                    break
                else:
                    result = result + item
            continue
        if priority(string[i]) == 0:
            result = result + string[i]
            continue
        if priority(string[i]) != 0:
            while len(stack) > 0 and priority(stack[-1]) >= priority(string[i]):
                result = result + stack.pop()
            stack.append(string[i])
    while len(stack) > 0:
        result = result + stack.pop()
    return result


class TestCase(unittest.TestCase):
    def test_sample(self):
        dataT = [("a+b*(c^d-e)^(f+g*h)-i", "abcd^e-fgh*+^*+i-")]
        for item in dataT:
            result = infix_to_postfix(item[0])
            self.assertEqual(result, item[1])


def main():
    t = int(input())
    for i in range(t):
        string = input()
        print(infix_to_postfix(string))


if __name__ == "__main__":
    unittest.main()
