"""
https://practice.geeksforgeeks.org/problems/sum-string/0

Given a string of digits, the task is to check if it is a ‘sum-string’. A string S is called a sum-string if a rightmost substring can be written as sum of two substrings before it and same is recursively true for substrings before it.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string S as input.

Output:
For each test case, print "1", if the string is sum-string else print "0".


Constraints:
1<=T<=100
1<=S<=105

Example:
Input:
3
12243660
1111112223
2368

Output:
1
1
0

Explanation:

 In 1st test case 
"12243660" is a sum string. 
As we can get, 24 + 36 = 60 & 12 + 24 = 36
 In 2nd test case
"1111112223" is a sum string. 
As we can get, 111+112 = 223 & 1+111 = 112

"""

def Int(s):
    if len(s) == 0:
        return 0
    return int(s)

def isvalidString(string,st):
    
    if string == '':
        return True
    
    n = len(st)
    if st != string[:n]:
        return False
    
    new_string = string[n:]

    for i in range(0,len(new_string)):
        if isvalidString(new_string[i+1:],str(Int(st)+Int(new_string[:i]))):
            return True
    
    return False

if __name__ == '__main__':
   st = "1111112223"
   print(isvalidString(st,''))

    
