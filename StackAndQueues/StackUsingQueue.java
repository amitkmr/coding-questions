
import java.util.*;
class StackUsingQueues
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
                int QueryType = sc.nextInt();
                if(QueryType == 1)
                {
                    int a = sc.nextInt();
                    g.push(a);
                }
                else if(QueryType == 2)
                System.out.print(g.pop()+" ");
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
    Queue<Integer> q1 = new LinkedList<Integer>();
    Queue<Integer> q2 = new LinkedList<Integer>();
    
    /*The method pop which return the element poped out of the stack*/
    int pop()
    {
        int lastElement = -1;
        if(q1.size()==0){
            while(q2.size()>0){
                lastElement = q2.poll();
                if(q2.size()!=0)
                    q1.add(lastElement);
            }
        }
        else{
            while(q1.size()>0){
                lastElement = q1.poll();
                if(q1.size()!=0)
                    q2.add(lastElement);
            }
        }
        
        return lastElement;
    }
    
    /* The method push to push element into the stack */
    void push(int a)
    {
        if(q1.size()>0){
            q1.add(a);
            return;
        }  
            
        if(q2.size()>0){
            q2.add(a);
            return;
        }
        
        q1.add(a);
    }
}