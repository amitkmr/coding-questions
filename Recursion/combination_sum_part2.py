"""
https://practice.geeksforgeeks.org/problems/combination-sum-part-2/0

Given an array of integers A and a sum B, find all unique combinations in A where the sum is equal to B.

ach number in A may only be used once in the combination.

Note:
   All numbers will be positive integers.
   Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
   The combinations themselves must be sorted in ascending order.
   If there is no combination possible the print "Empty" (without qoutes).
Example,
Given A = 10,1,2,7,6,1,5 and B(sum) 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

Input:
First is T , no of test cases. 1<=T<=500
Every test case has three lines.
First line is N, size of array. 1<=N<=12
Second line contains N space seperated integers(x). 1<=x<=9.
Third line is the sum B. 1<=B<=30.
 
Output:
One line per test case, every subset enclosed in () and in every set intergers should be space seperated.(See example)

Example:
Input:
2
7
10 1 2 7 6 1 5
8
5
8 1 8 6 8
12

Output:
(1 1 6)(1 2 5)(1 7)(2 6)
Empty

"""
def to_tuple(arr):
    if len(arr) == 0:
        return ""
    result = "("
    comma_flag = True
    for item in arr:
        if comma_flag:
            comma_flag = False
            result = result + str(item)
        else:
            result = result + " " + str(item)
    return result + ")"
        

def combination_sum(prefix,rem,given_sum):
    prefix_sum = sum(prefix)
    difference = given_sum - prefix_sum
    if difference < 0:
        return ""
    if difference == 0:
        return to_tuple(prefix)

    result = ""
    prev = None
    for i in range(0,len(rem)):
        item = rem[i]
        if prev and prev == item:
            prev = item
            continue
        if prefix_sum + item > given_sum:
            break
        result = result + combination_sum(prefix+[item],rem[i+1:],given_sum)
        prev = item
    return result

        


def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip().split(" ")]
        given_sum = int(input())
        result = combination_sum([],sorted(arr),given_sum)
        if len(result) == 0:
            print("Empty")
        else:
            print(result)

if __name__ == '__main__':
    main()
    