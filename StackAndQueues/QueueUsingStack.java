/*
url : https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1

Implement a Queue using 2 stacks s1 and s2 .

Input (To be used for Expected Output):

The first line of the input contains an integer 'T' denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer Q denoting the number of queries . 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)

The second line of each test case contains Q queries seperated by space.

Output:
The output for each test case will  be space separated integers having -1 if the queue is empty else the element poped out from the queue . 
You are required to complete the two methods push which take one argument an integer 'x' to be pushed into the quee  and pop which returns a integer poped out from othe queue.

Constraints:
1<=T<=100
1<=Q<=100
1<=x<=100

Example:
Input
1
5
1 2 1 3 2 1 4 2   

Output
2 3

Explanation:

In the first test case for query 
1 2    the quee will be {2}
1 3    the queue will be {2 3}
2       poped element will be 2 the queue will be {3}
1 4    the queue will be {3 4}
2       poped element will be 3 

*/


import java.util.*;
import java.util.Stack;
import java.util.LinkedList;
class Queue_Using_Two_Stacks
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t>0)
        {
            GfG g = new GfG();
            int q = sc.nextInt();
            while(q>0)
            {
                int QueryTyoe = sc.nextInt();
                if(QueryTyoe == 1)
                {
                    int a = sc.nextInt();
                    g.insert(a);
                }else
                if(QueryTyoe == 2)
                System.out.print(g.remove()+" ");
            q--;
                
            }
            System.out.println();
        t--;
        }
    }
}
    
    /*Please note that it's Function problem i.e.
    you need to write your solution in the form of Function(s) only.
    Driver Code to call/invoke your function is mentioned above.*/
    
class GfG
{
    Stack<Integer> s1 = new Stack<Integer>();
    Stack<Integer> s2 = new Stack<Integer>();
    /* The method insert to push element into the queue */
    void insert(int B)
    {
        s1.push(B);
    // Your code here
    }
    
    
    /*The method remove which return the element popped out of the queue*/
    int remove()
    {
        if(s2.isEmpty()){
            while(!s1.isEmpty())
                s2.push(s1.pop());
        }
        
        if(s2.isEmpty())
            return -1;
        return s2.pop();
    // Your code here
    }
}