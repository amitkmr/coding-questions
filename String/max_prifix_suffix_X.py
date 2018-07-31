"""
https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0

Given a string of character, find the length of longest proper prefix which is also a proper suffix.
Example:
S = abab
lps is 2 because, ab.. is prefix and ..ab is also a suffix.

Input:
First line is T number of test cases. 1<=T<=100.
Each test case has one line denoting the string of length less than 100000.

Expected time compexity is O(N).

Output:
Print length of longest proper prefix which is also a proper suffix.

Example:
Input:
2
abab
aaaa

Output:
2
3

"""







def max_prerix_suffix(st):
    n =len(st)
    i = 0
    j = 1
    result = [0]*len(st)
    while(j<n):
        if st[i] == st[j]:
            if i == 0:
                result[j] = 1
            else:
                result[j] = result[j-1] + 1
            i+=1
            j+=1
            continue
        
        if st[i] != st[j] and i != 0:
            j = j-1
            
        i = 0
        j+=1
       
    return result[n-1]
    
def main():
    t = int(input())
    for i in range(t):
        st = input()
        print(max_prerix_suffix(st))

if __name__ == '__main__':
    main()