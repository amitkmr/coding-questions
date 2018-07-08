"""
https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

Given a linked list, the task is to find the n'th node from the end.  It is needed to complete a method that takes two argument, head of linked list and an integer n. There are multiple test cases. For each test case, this method will be called individually.


Input:
The first line of input contains number of test cases.  Every test case cntains two lines.  First line of every test case contains two space separated values, number of nodes  in linked list followed by value of n.  Second line of every test case contains data items of linked list.


Output:
Corresponding to each test case, output a single integer that is the nth integer in the linked list from the end. Print -1 if the value of n is greater than the number of elements in the linked list.

Constraints:
1 <= T <= 200
1 <= No of Nodes <= 1000
0 <= Data in Nodes <= 1000


Example:
Input:
2
9 2
1 2 3 4 5 6 7 8 9
4 5
10 5 100 5 1
 

Output:
8
-1
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return index to the any valid peak element

def reverseList(head):
    # Code here
    if head is None:
        return None
    
    node = head
    prev = None

    while(node):
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    return prev

def getNthFromLast(head, n):
    node = reverseList(head)
    count = 1
    while(node and count<n):
        count = count + 1
        node = node.next
    if node == None:
        return -1
    else:
        return node.data

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(getNthFromLast(head, k))
# Contributed by: Harshit Sidhwa

