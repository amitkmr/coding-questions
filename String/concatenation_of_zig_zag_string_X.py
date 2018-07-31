"""
https://practice.geeksforgeeks.org/problems/concatenation-of-zig-zag-string-in-n-rows/0


Given a string and number of rows ‘n’. Print the string formed by concatenating n rows when input string is written in row-wise Zig-Zag fashion.

Examples:

Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G   
  B   D   F   H
Now concatenate the two rows and ignore spaces 
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces 
in every row. We get "GSGSEKFREKEOE"
 

Input:

The first line of input consists number of the test cases. The description of T test cases is as follows:

The first line of each test case contains the string, and the second line has 'n' the number of rows.


Output:

In each separate line print the string after concatenating n rows in a zig zag form.


Constraints:

1 ≤ T ≤ 70
1 ≤ N ≤ size of string


Example:

Input:

2
qrrc
3
rfkqyuqfjkxy
2

Output:

qrcr
rkyqjxfqufky

"""

def zigzag_string(st,k):
    
    diff = 2* k - 2

    result = ""
    for i in range(k):
        j = 0 
        while(j+i<len(st)):
            result+=st[j+i]
            j+=diff
    print(result)

def main():
    t = int(input())
    for i in range(t):
        st = input()
        k = int(input())
        zigzag_string(st,k)

if __name__ == '__main__':
    main()
    