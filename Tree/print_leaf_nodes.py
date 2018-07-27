"""
Print leaf nodes from preorder traversal of BST
Given a preorder traversal of a BST, print the leaf nodes of the tree without building the tree.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of nodes of the BST. Then in the next line are N space separated values denoting the preorder traversal of the binary tree.

Output:
For each test case in a new line print the leaf nodes separated by space of the BST in sorted order.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
5
890 325 290 530 965 
3
3 2 4

Output:
290 530 965
2 4
"""

def print_leafs(arr):
    if len(arr) == 0:
        return

    pivot = arr[0]
    if len(arr) == 1:
        print(pivot,end= " ")
        return
    i = 1
    while(i<len(arr)):
        if arr[i] > pivot:
            break
        i = i + 1
    print_leafs(arr[1:i])
    print_leafs(arr[i:])    

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print_leafs(arr)
        print()

if __name__ == '__main__':
    main()
    
# 45
# 61 8 48 767 675 465 323 95 91 212 156 201 210 240 265 261 270 401 393 388 425 558 556 502 478 598 563 587 646 621 754 689 686 696 713 702 757 993 967 870 837 829 925 920 999
# Need Help ?

# 48 91 210 261 270 388 425 478 587 621 686 702 757 829 920 999
# 48 91 210 261 270 388 425 502 478 587 621 686 702 757 829 925 920 999


