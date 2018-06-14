"""
Given a String of length N reverse the words in it. Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. Each case contains a string containing spaces and characters.
 

Output:
For each test case, output a single line containing the reversed String.

Constraints:
1<=T<=20
1<=Lenght of String<=2000


Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
"""


def reverse_words(string):
    str_arr = string.split(".")
    print(".".join(str_arr[::-1]))

t = int(input())

for i in range(0,t):
    string = input()
    reverse_words(string)