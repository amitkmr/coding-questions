/*

          
Given a Binary Tree,  print the bottom view from left to right. A node x is there in output if x is the bottommost node at its horizontal distance from root. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

Examples:

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree the output should be 5, 10, 3, 14, 25.

If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottom-most nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5, 10, 4, 14, 25.

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print nodes in bottom view of Binary Tree.  Your code should not print a newline, it is added by the caller code that runs your function.

Constraints:
1 <=T<= 30
0 <= Number of nodes<= 100
0 <= Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
3 1 2
40 20 60 30

There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.

*/

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

class Print_Bottom_View {
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
            // bottom_view
            g.bottomView(root);
            
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

    public void traverseTree(Node root,int position, Map<Integer, Integer> bottomMap){
      if (root == null)
        return;
      bottomMap.put(position, root.data);
      traverseTree(root.left, position-1, bottomMap);
      traverseTree(root.right, position+1, bottomMap);
    }

    // Should print bottom view of tree with given root
    public void bottomView(Node root)
    {
        Map<Integer,Integer> bottomMap = new TreeMap<Integer,Integer>();
        
        traverseTree(root, 0, bottomMap);
        for(Map.Entry m:bottomMap.entrySet()){  
          System.out.print(m.getValue()+" ");  
        }
        System.out.println("");
    }
}

    