"""
https://practice.geeksforgeeks.org/problems/transform-string/0

You are provided two strings A and B. You have to transform string A into string B in minimum number of steps. Only one operation is allowed, chose any of the characters in string A and place it in the front of A. If its not possible to transform string A into string B then print -1 otherwise print the minimum number of steps required.

Note: All the characters in the string are lowercase English characters.

Input :

The first line contains integer T, denoting number of test cases. Then T test cases follow . 
The first line of each test case contains two space separated  strings A and B.

Output:
Print in a new line the answer of each test case .

Constraints :

1<=T<=100

1<=|A|,|B|<=10^5

Example:
Input:
2
bcad abcd
abdd dbad

Output :
1
2

"""
# longest common subsequence
def lcs(s1,s2,m,n):
    if m<0 or n<0:
        return 0
    if s1[l] == s2[r]:
        return 1 + lcs(s1,s2,m-1, n-1)
    else:
        return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))

def transfrom_cost(s1,s2):
    if sorted(s1) != sorted(s2):
        return -1
    return len(s1) - lcs(s1,s2,len(s1)-1,len(s2)-1)
    

def main():
    t = int(input())
    for i in range(t):
        st1,st2 = list(map(int,input.split()))
        print(transfrom_cost(st1,st2))
if __name__ == '__main__':
    main()
    