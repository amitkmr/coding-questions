"""
https://practice.geeksforgeeks.org/problems/josephus-problem/1

Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.​ The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive. You are required to complete the function josephus which returns an integer denoting such position . 

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. Each test case contains 2 integers n and k .

Output:
For each test case in a new line output will be the safe position which satisfies the above condition.

Constraints:
1<=T<=100
1<=k,n<=20

Example(To be used only for expected output) :
Input:
2
3 2
5 3

Output
3
4

"""



''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Your function should return an integer 
def find_position(arr,k,start):
    if len(arr) == 1:
        return arr[0]
    
    index = (start+k-1)%len(arr)
    arr.pop(index)
    
    return find_position(arr,k,(index)%len(arr))
        
def josephus(n, k):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    return find_position(arr,k,0)
    

#Your Code goes here
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        print(josephus(n ,k))
# contributed by:Harshit Sidhwa