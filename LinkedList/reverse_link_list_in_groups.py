"""
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

Given a linked list, write a function to reverse every k nodes (where k is an input to the function).If a linked list is given as 1->2->3->4->5->6->7->8->NULL and k = 3 then output will be 3->2->1->6->5->4->8->7->NULL.

Input:
In this problem, method takes two argument: the head of the linked list and int k. You should not read any input from stdin/console.
The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
Reverse the linked list in the group of given size and return the reference of starting node(head) of the reversed Linked list .

Note: If you use "Test" or "Expected Output Button" use below example format
Example:
Input:
1
8
1 2 2 4 5 6 7 8
4

Output:
4 2 2 1 8 7 6 5

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""

def reversek(head,k):
    prev = None
    node = head
    i = 0
    while(node and i<k):
        i = i + 1
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    
    return prev,head

    # Code here
def reverse(head, k):
    
    counter_node = head
    tail = None
    new_head = None
    while(counter_node):
        i = 0
        start_node = counter_node
        while(counter_node and i<k):
            i = i + 1
            counter_node = counter_node.next
        head,last = reversek(start_node,k)
        if new_head == None:
            new_head = head
            
        if tail:
            tail.next = head
        tail = last
    return new_head

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
