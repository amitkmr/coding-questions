/*
Given a binary tree, find if it is height balanced or not.  A tree is heigh balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree.    Expected time complexity is O(n).

A height balanced tree
        1
     /     \
   10      39
  /
5

An unbalanced tree
        1
     /    
   10   
  /
5

 

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should return true if tree is height balanced, else false.

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input:
2
2
1 2 L 2 3 R
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
0
1
*/

import java.util.Scanner;

import jdk.nashorn.internal.ir.ReturnNode;

import java.util.*;
import java.lang.*;
import java.io.*;

class Node {
    int data;
    Node left, right;

    Node(int d) {
        data = d;
        left = right = null;
    }
}

class Height_Balanced_Tree {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            HashMap<Integer, Node> m = new HashMap<Integer, Node>();
            int n = sc.nextInt();
            Node root = null;
            while (n > 0) {

                int n1 = sc.nextInt();
                int n2 = sc.nextInt();
                char lr = sc.next().charAt(0);

                // cout << n1 << " " << n2 << " " << (char)lr << endl;
                Node parent = m.get(n1);
                if (parent == null) {
                    parent = new Node(n1);
                    m.put(n1, parent);
                    if (root == null)
                        root = parent;
                }
                Node child = new Node(n2);
                if (lr == 'L')
                    parent.left = child;
                else
                    parent.right = child;
                m.put(n2, child);
                n--;
            }

            GfG g = new GfG();

            // boolean res = g.isHeap(root);
            if (g.isBalanced(root) == true)
                System.out.println(1);
            else
                System.out.println(0);
            // CLN.inorder(root);
            t--;
            // System.out.println();
        }
    }
}

/*
 * Please note that it's Function problem i.e. you need to write your solution
 * in the form of Function(s) only. Driver Code to call/invoke your function is
 * mentioned above.
 */

/*
 * A binary tree node class class Node { int data; Node left,right;
 * 
 * Node(int d) { data = d; left = right = null; } }
 */
class GfG {

    int height(Node root){
        if (root == null)
            return 0;
        return 1 + Math.max(height(root.left), height(root.right));
    }

    /*
     * This function should return tree if passed tree is balanced, else false. Time
     * complexity should be O(n) where n is number of nodes in tree
     */
    boolean isBalanced(Node root) {
        if(root== null)
            return true;
        // Your code here
        if (Math.abs(height(root.left)-height(root.right)) > 1)
            return false;
        return isBalanced(root.left) && isBalanced(root.right);
            
    }
}
