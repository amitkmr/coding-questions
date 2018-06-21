"""
url : 
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.

Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains
two space separated integers N and S, where N is the number of digits and S is the sum.

Output

Print the largest number that is possible.
If their is no such number, then print -1

Constraints:

1 <= T <= 30
1 <= N <= 50
0 <= S <= 500

Example

Input
2
2 9
3 20

Output

90
992
Expected Time Complexity: O(n)

"""

def largest_number(n,s):
    if s==0:
        return -1
    digit = 9
    number = ""
    while(s>=0 and digit >=0 and len(number)<n):
        if s-digit >= 0:
            s = s - digit
            number = number + str(digit)
        else:
            digit = digit - 1
    if s>0:
        return -1
    else:
        return number
        

def main():
    t = int(input().strip())
    for i in range(0,t):
        numbers = input().strip().split(" ")
        n = int(numbers[0])
        k = int(numbers[1])
        print(largest_number(n,k))

if __name__ == '__main__':
    main()