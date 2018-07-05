"""
https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0

Given an input stream of n characters consisting only of small case alphabets the task is to find the first non repeating character each time a character is inserted to the stream. If no non repeating element is found print -1.

Example

Flow in stream : a, a, b, c
a goes to stream : 1st non repeating element a (a)
a goes to stream : no non repeating element -1 (a, a)
b goes to stream : 1st non repeating element is b (a, a, b)
c goes to stream : 1st non repeating element is b (a, a, b, c)

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the stream. Then in the next line are x characters which are inserted to the stream.

Output:
For each test case in a new line print the first non repeating elements separated by spaces present in the stream at every instinct when a character is added to the stream, if no such element is present print -1.

Constraints:
1<=T<=200
1<=N<=500

Example:
Input:
2
4
a a b c
3
a a c 
Output:
a -1 b b
a -1 c
"""

def non_repeating(arr,n):
    chars = {}
    c = 0
    for i in range(n):
        if arr[i] in chars.keys():
            chars[arr[i]] = chars[arr[i]] + 1
        else:
            chars[arr[i]] = 1
        
        while(c<=i):
            if chars[arr[c]] == 1:
                print(arr[c],end=" ")
                break
            else:
                c = c + 1
        if c > i:
            print(-1,end=" ")
        

    print()
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip(" ").split(" ")
        non_repeating(arr,n)

if __name__ == '__main__':
    main()
    