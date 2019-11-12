import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct_tree(inorder, preorder):
    if len(preorder) == 0:
        return None

    data = preorder[0]
    indexOfInorder = inorder.index(data)
    node = Node(data)
    node.left = construct_tree(
        inorder[:indexOfInorder], preorder[1 : indexOfInorder + 1]
    )

    node.right = construct_tree(
        inorder[indexOfInorder + 1 :], preorder[indexOfInorder + 1 :]
    )

    return node


def print_preorder(tree):
    if not tree:
        return

    print(tree.data, end=" ")

    print_preorder(tree.left)
    print_preorder(tree.right)


class TestCase(unittest.TestCase):
    def test_sample(self):
        inOrder = ["D", "B", "E", "A", "F", "C"]
        preOrder = ["A", "B", "D", "E", "C", "F"]

        result = construct_tree(inOrder, preOrder)

        print_preorder(result)
        print("")


if __name__ == "__main__":
    unittest.main()
