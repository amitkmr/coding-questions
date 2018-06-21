import java.util.*;
class Get_Min_From_Stack
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T>0)
        {
            int q = sc.nextInt();
            GfG g = new GfG();
            while(q>0)
            {
                int qt = sc.nextInt();
                
                if(qt == 1)
                {
                    int att = sc.nextInt();
                    g.push(att);
                    //System.out.println(att);
                }
                else if(qt == 2)
                {
                    System.out.print(g.pop()+" ");
                }
                else if(qt == 3)
                {
                    System.out.print(g.getMin()+" ");
                }
            
            q--;
            }
            System.out.println();
        T--;
        }
        
    }
}
    
    /*Please note that it's Function problem i.e.
    you need to write your solution in the form of Function(s) only.
    Driver Code to call/invoke your function is mentioned above.*/
    
class GfG
{
    int minEle;
    Stack<Integer> s = new Stack<Integer>();
    Stack<Integer> minStack = new Stack<Integer>();
    /*returns min element from stack*/
    int getMin()
    {
        if (minStack.isEmpty())
            return -1;
        return minStack.peek();
    }
    
    /*returns poped element from stack*/
    int pop()
    {
        if(s.isEmpty())
            return -1;
        minStack.pop();
        return s.pop();
    }
    /*push element x into the stack*/
    void push(int x)
    {
        s.push(x);
        if(minStack.isEmpty() || minStack.peek()>x){
            minStack.push(x);
        }
        else{
            minStack.push(minStack.peek());
        }
    }	
}