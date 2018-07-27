"""
Preorder Traversal and BST
Given an array, write a program that prints 1 if given array can represent preorder traversal of a BST, else prints 0.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input A[i].

Output:
Should print 1 if given array can represent preorder traversal of BST. Otherwise 0.

Constraints:
1 <=T<= 55
1 <= N <= 1000
1 <= arr[i] <= 1000

Example:

Input:
3
5
40 30 35 80 100
8
40 30 32 35 80 90 100 120
8
7  9 6 1 4 2 3 40

Output:
1
1
0

"""

def is_preorder_traversal(arr):
    if len(arr) == 0:
        return True

    pivot = arr[0]

    i = 1
    split_index = len(arr)
    while(i<len(arr)):
        if arr[i] > pivot:
            split_index = i
            break
        i = i + 1
    
    while(i<len(arr)):
        if arr[i] < pivot : 
            return False
        i = i + 1
    
    return is_preorder_traversal(arr[1:split_index]) and is_preorder_traversal(arr[split_index:])
    

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        if is_preorder_traversal(arr) :
            print("1")
        else:
            print("0")

if __name__ == '__main__':
    main()
    
# 45
# 61 8 48 767 675 465 323 95 91 212 156 201 210 240 265 261 270 401 393 388 425 558 556 502 478 598 563 587 646 621 754 689 686 696 713 702 757 993 967 870 837 829 925 920 999
# Need Help ?

# 48 91 210 261 270 388 425 478 587 621 686 702 757 829 920 999
# 48 91 210 261 270 388 425 502 478 587 621 686 702 757 829 925 920 999


