"""
https://practice.geeksforgeeks.org/problems/rearrange-characters/0

Given a string with repeated characters, task is to rearrange characters in a string such that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.


Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a single line containing a string of lowercase english alphabets.

Output:
For each test case in a new line print 1 if the generated sting doesn't contains any same adjacent characters, else if no such string is possible to be made print 0.
Constraints:
1<=T<=100
1<=length of string<=600

Example:
Input:
3
geeksforgeeks
bbbabaaacd
bbbbb

Output:
1
1
0

"""

def rearrange_char(st):
    rem = [0]*26
    for char in st:
        rem[ord(char)-ord('a')]+=1
    
    max_val = max(rem)
    print(rem)
    
    if max_val >= len(st)//2 + 1:
        return 0
    return 1

def main():
    t = int(input())
    for i in range(t):
        st = input()
        print(rearrange_char(st))

if __name__ == '__main__':
    main()
    