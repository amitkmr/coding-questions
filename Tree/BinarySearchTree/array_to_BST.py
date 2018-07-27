"""
Array to BST
Given a sorted array. Write a program that creates a Balanced Binary Search Tree using array elements. If there are n elements in array, then floor(n/2)'th element should be chosen as root and same should be followed recursively.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[].

Output:

Print the preorder traversal of constructed BST.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[] ≤ 10000

Example:

Input:
1
7
1 2 3 4 5 6 7

Output:
4 2 1 3 6 5 7

"""

import math

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def print_preorder(root):
    if root == None:
        return
    print(root.data,end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


def array_to_BST(arr):
    if len(arr) == 0:
        return None
    mid = math.floor(len(arr)/2)
    node = Node(arr[mid])

    node.left = array_to_BST(arr[:mid])
    node.right = array_to_BST(arr[mid+1:])
    return node

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        root = array_to_BST(arr)
        print_preorder(root)
        print()
if __name__ == '__main__':
    main()

"""
Input:
84
27 59 336 364 492 540 545 846 886 925 1087 1313 1393 1421 1530 1729 1873 2305 2362 2567 2777 2862 3058 3069 3135 3367 3426 3526 3750 3784 3895 3926 3929 4022 4043 4067 4324 4370 4421 4919 5011 5123 5198 5211 5368 5386 5434 5736 5782 5788 5857 6091 6124 6229 6327 6413 6429 6505 6649 6808 6862 6915 6996 7084 7178 7276 7281 7373 7763 7793 8042 8167 8315 8335 8456 8537 8690 8814 8980 9170 9172 9582 9802 9956

Its Correct output is:
5123 2777 925 492 59 27 336 364 545 540 846 886 1530 1313 1087 1393 1421 2305 1729 1873 2362 2567 3895 3367 3058 2862 3069 3135 3526 3426 3750 3784 4067 3929 3926 4022 4043 4421 4324 4370 4919 5011 6996 6091 5434 5211 5198 5368 5386 5782 5736 5788 5857 6429 6229 6124 6327 6413 6808 6505 6649 6862 6915 8335 7373 7178 7084 7276 7281 8042 7763 7793 8167 8315 8980 8537 8456 8690 8814 9582 9170 9172 9802 9956

And Your Code's output is:
5198 2862 1087 540 336 59 27 492 364 886 846 545 925 1873 1421 1393 1313 1729 1530 2567 2362 2305 2777 3929 3526 3135 3069 3058 3426 3367 3895 3784 3750 3926 4370 4067 4043 4022 4324 5011 4919 4421 5123 7084 6229 5782 5386 5368 5211 5736 5434 6091 5857 5788 6124 6649 6429 6413 6327 6505 6915 6862 6808 6996 8456 7793 7281 7276 7178 7763 7373 8315 8167 8042 8335 9170 8814 8690 8537 8980 9802 9582 9172 9956

"""
    
    