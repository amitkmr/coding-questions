"""

Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have any adjacent duplicates.
 

Input:
The first line of input contains an integer T, denoting the no of test cases. Then T test cases follow. Each test case contains a string str.

Output:
For each test case, print a new line containing the resulting string.

Constraints:
1<=T<=100
1<=Length of string<=50

Example:
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac

"""

def remove_adjacent_duplicates(string):
    
    prev = 0
    seq = []
    
    for i in range(1,len(string)):
        if string[prev] == string[i]:
            continue
        else:
            if prev != i-1:
                seq.append((prev,i))
            prev = i
    
    if prev != len(string)-1:
        seq.append((prev,len(string)))
    
    result = ""

    start = 0
    for item in seq:
        result = result + string[start:item[0]]
        start = item[1]
    result = result + string[start:len(string)]
    
    if result == string:
        return string
    else:
        return remove_adjacent_duplicates(result)

t = int(input())

for i in range(0,t):
    string = input()
    print(remove_adjacent_duplicates(string))