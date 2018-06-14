"""
Given a string, print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases.
Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG
Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA


"""

def permutations(prefix,string):
    if string == "":
        print(prefix,end=" ")
        return
    for i in range(0,len(string)):
        permutations(prefix+string[i],string[:i]+string[i+1:])
    


t = int(input())
for i in range(0,t):
    string = input()
    permutations("","".join(sorted(string)))
    print()