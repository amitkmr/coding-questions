""" 
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.
 
Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. Each test case contains a string str .

Output:
For each test case in a new line output will be an integer denoting the converted integer, if the input string is not a numerical string then output will be -1.
 
Constraints:
1<=T<=100
1<=length of (s,x)<=10

Example(To be used only for expected output) :
Input:
2
123
21a

Output:
123
-1
"""
def atoi(string):
    number = 0
    flag = 1
    for i in string:
        if i == '-':
            flag = -1
            continue
        
        t = ord(i)-ord('0')
        if t>9:
            return -1
        number = number*10 + t
    return number * flag