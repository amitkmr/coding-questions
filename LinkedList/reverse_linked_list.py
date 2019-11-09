import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(reversed, remain):
    if not remain:
        return reversed
    next = remain.next
    remain.next = reversed
    reversed = remain

    return reverse(reversed, next)


def print_linked_list(link: Node):
    while link:
        print(f"{link.data} -> ", end="")
        link = link.next
    print(f"Null")


class TestCase(unittest.TestCase):
    def test_reverse(self):
        head = None
        for i in range(10, 0, -1):
            node = Node(i)
            node.next = head
            head = node

        result = reverse(None, head)
        print_linked_list(result)


if __name__ == "__main__":
    unittest.main()
