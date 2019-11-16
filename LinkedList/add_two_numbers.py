import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def node_value(node):
    if node:
        return node.data
    else:
        return 0


def add_digits(d1, d2, c=0):
    return (d1 + d2 + c) // 10, (d1 + d2 + c) % 10


def add(carry, list1, list2):
    if carry == 0 and list1 == None and list2 == None:
        return None

    carry, value = add_digits(node_value(list1), node_value(list2), carry)
    node = Node(value)
    if list1:
        list1 = list1.next

    if list2:
        list2 = list2.next

    node.next = add(carry, list1, list2)
    return node


def print_linked_list(link: Node):
    while link:
        print(f"{link.data} -> ", end="")
        link = link.next
    print(f"Null")


class TestCase(unittest.TestCase):
    def test_reverse(self):
        list1 = None
        for i in [7, 5, 9, 4, 6][::-1]:
            node = Node(i)
            node.next = list1
            list1 = node

        list2 = None
        for i in [8, 4][::-1]:
            node = Node(i)
            node.next = list2
            list2 = node

        print_linked_list(list1)
        print_linked_list(list2)
        result = add(0, list1, list2)
        print_linked_list(result)


if __name__ == "__main__":
    unittest.main()
