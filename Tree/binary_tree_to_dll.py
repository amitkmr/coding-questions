"""
             
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

TreeToList

Input:
The task is to complete the method which takes two arguments, root of Binary Tree and reference to head of DLL.

The struct Node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should change reference of head to head of linked list. 

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:

3 1 2 
2 1 3 
40 20 60 10 30 
30 10 60 20 40 
There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 2 and right child of 1 is 3.   Second test case represents a tree with 4 edges and 5 nodes. 
The output of complete program is forward and backword traversals of modified linked list.

"""

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
class Tree:  #Binary tree Class
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if(ch=='L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right
    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i
    def traverseInorder(self, root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data, end=" ")
            self.traverseInorder(root.right)
import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#function should return head to the DLL
def convertToDDL(root,next):
    if root.right != None:
        right_node = convertToDDL(root.right,next)
        right_node.left = root
        root.right = right_node
    else:
        root.right = next
        if next != None:
            next.left = root
    
    if root.left != None:
        left_node = convertToDDL(root.left,root)
        return left_node
    else:
        return root
        
        
def BTToDLL(root):
    if root == None:
        return None
        
    return convertToDDL(root,None)
    

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        tree = Tree()
        lis=[]
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k=0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            # print arr[k], arr[k+1], ptr
            k+=3
        # tree.traverseInorder(root)
        # print ''
        head = None #head to the DLL
        head = BTToDLL(root)
        printDLL(head),
# Contributed by: Harshit Sidhwa
    
