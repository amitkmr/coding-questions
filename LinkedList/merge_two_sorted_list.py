import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    if list1.data < list2.data:
        list1.next = merge(list1.next, list2)
        return list1
    else:
        list2.next = merge(list1, list2.next)
        return list2


def print_linked_list(link: Node):
    while link:
        print(f"{link.data} -> ", end="")
        link = link.next
    print(f"Null")


class TestCase(unittest.TestCase):
    def test_reverse(self):
        list1 = None
        for i in range(10, 0, -2):
            node = Node(i)
            node.next = list1
            list1 = node

        list2 = None
        for i in range(9, 0, -2):
            node = Node(i)
            node.next = list2
            list2 = node

        print_linked_list(list1)
        print_linked_list(list2)
        result = merge(list1, list2)
        print_linked_list(result)


if __name__ == "__main__":
    unittest.main()
