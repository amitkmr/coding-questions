
/*

Serialization is to store a tree in an array so that it can be later restored and Deserialization is reading tree back from the array. Now your task is to complete the function serialize which stores the tree into an array A[ ] and deSerialize which deserializes the array to tree and returns it.

Note: The structure of tree must be maintained.

Input:
The task is to complete two method serialize and deSerialize.  The method serialize takes  two arguments, the first is the root of Binary Tree and second argument is an array A[ ] which stores the serialized tree. The method deSerialize takes only one argument which is the serialized array A[] and returns the deserialzed tree's root . The struct Node has a data part which stores the data, pointer to left child and pointer to right child.There are multiple test cases. For each test case, this method will be called individually.

Output:
The  output in the expected output will be the inorder traversal of the returned tree .

Constraints:
1 <=T<= 30
1 <= Number of nodes<= 100
1 <= Data of a node<= 100

Example(To be used only for expected output):
Input
2
2
1 2 L 1 3 R
4
10 20 L 10 30 R 20 40 L 20 60 R

Output
2 1 3
40 20 60 10 30



There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.

*/

import java.util.*;
import java.util.stream.Collectors;

// import jdk.nashorn.internal.ir.ReturnNode;

class Tree {
	int data;
	Tree left, right;

	Tree(int d) {
		data = d;
		left = right = null;
	}
}

class SND {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while (t-- > 0) {
			int n = sc.nextInt();
			Tree root = null;
			if (n == 1) {
				System.out.println(sc.nextInt());
				n--;
			}
			while (n-- > 0) {
				int n1 = sc.nextInt();
				int n2 = sc.nextInt();
				char lr = sc.next().charAt(0);
				if (root == null) {
					root = new Tree(n1);
					switch (lr) {
					case 'L':
						root.left = new Tree(n2);
						break;
					case 'R':
						root.right = new Tree(n2);
						break;
					}
				} else {
					insert(n1, n2, lr, root);
				}
			}
			ArrayList<Integer> aa = new ArrayList<Integer>();
			GfG g = new GfG();
			String s = g.serialize(root, aa);
			Tree root1 = g.deSerialize(s);
			inorder(root1);
			System.out.println();
		}
	}

	public static void inorder(Tree root) {
		if (root == null)
			return;
		inorder(root.left);
		System.out.print(root.data + " ");
		inorder(root.right);
	}

	public static void insert(int n1, int n2, char lr, Tree root) {
		if (root == null) {
			return;
		}
		if (root.data == n1) {
			switch (lr) {
			case 'L':
				root.left = new Tree(n2);
				break;
			case 'R':
				root.right = new Tree(n2);
				break;
			}
		}
		insert(n1, n2, lr, root.left);
		insert(n1, n2, lr, root.right);
	}
}

/*
 * Please note that it's Function problem i.e. you need to write your solution
 * in the form of Function(s) only. Driver Code to call/invoke your function is
 * mentioned above.
 */

/*
 * Complete the given function Node is as follows: class Tree{ int data; Tree
 * left,right; Tree(int d){ data=d; left=right=null; } }
 */
class GfG {

	public void traversePreOrder(Tree root,ArrayList<Integer>aa){
		if (root == null){
			aa.add(-1);
			return;
		}
		aa.add(root.data);
		traversePreOrder(root.left,aa);
		traversePreOrder(root.right,aa);
	}

	public String serialize(Tree root, ArrayList<Integer> aa) {
		// add Code here.
		traversePreOrder(root,aa);
		String listString = aa.stream().map(Object::toString)
						.collect(Collectors.joining(","));
		return listString;
	}

	public Tree deSerialize(String data) {
		List<String> list = new ArrayList<String>(Arrays.asList(data.split(",")));

		Stack<Tree> stack = new Stack<Tree>();

		Tree root = null;

		Tree prevNode = null;
		Tree currentNode = null;
		for (String numbeString : list) {
			Integer item = Integer.parseInt(numbeString);
			if(item != -1){
				currentNode = new Tree(item);
				if(root == null)
					root = currentNode;
			}
			else
				currentNode = null;

			if (prevNode != null){
				prevNode.left = currentNode;
			}
			else{
				if(stack.isEmpty()== false){
					prevNode = stack.pop();
					prevNode.right = currentNode;
				}
			}

			prevNode = currentNode;
			if(currentNode != null)
				stack.push(currentNode);
		}
		return root;
	}
}