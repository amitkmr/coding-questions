"""

Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

 

Input:

The first line of input contains an integer T denoting the number of test cases. 
Each test case consist of a string of expression, in a separate line.

Output:

Print 'balanced' without quotes if pair of parenthesis are balanced else print 'not balanced' in a separate line.


Constraints:

1 ≤ T ≤ 100
1 ≤ |s| ≤ 100


Example:

Input:
3
{([])}
()
()[]

Output:
balanced
balanced
balanced

"""

def parenthesis_checker(string):
    stack = []
    for item in string:
        if item =='{' or item =='(' or item =='[':
            stack.append(item)
        elif item == '}':
            if len(stack)>0 and stack[-1] == '{':
               stack.pop()
            else:
                print("not balanced")
                return
        elif item == ')':
            if len(stack)>0 and stack[-1] == '(':
               stack.pop()
            else:
                print("not balanced")
                return
        elif item == ']':
            if len(stack)>0 and stack[-1] == '[':
               stack.pop()
            else:
                print("not balanced")
                return
        else:
            print("not balanced")
            return
    if len(stack) == 0:
        print("balanced")
    else:
        print("not balanced")

t = int(input())

for i in range(0,t):
    string = input()
    parenthesis_checker(string)