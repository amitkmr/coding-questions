"""
Your task  is to implement the function strstr. The function takes two strings as arguments(s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting  the first occurrence of the string x .
 
Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow. The first line of each test case contains two strings str and target.

Output:
For each test case in a new line output will be an integer denoting the first occurrence of the target  string in the string s. Return -1 if no match found.
 
Constraints:
1<=T<=100
1<=length of (s,x)<=1000

Example:
Input
2
GeeksForGeeks Fr
GeeksForGeeks For
Output
-1
5

"""

def strstr(str, substr):
      # code here
      
      for i in range(0,len(str)):
          j = 0
          k = i
          while(j<len(substr) and k < len(str) and  str[k]==substr[j]):
              j = j + 1
              k = k + 1
          if j == len(substr):
              return i
      return -1