"""
url : https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
Given a sequence, find the length of the longest increasing subsequence from a given sequence .
The longest increasing subsequence means to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest
to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

Note: Duplicate numbers are not counted as increasing subsequence.

For example:
 length of LIS for 
{ 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

 

Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the size of array and next line followed by the value of array.


Output:

Print the Max length of the subsequence in a separate line.


Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000
0 ≤ A[i] ≤ 300

Example:

Input
1
16
0 8 4  12 2 10 6  14 1 9 5  13 3 11 t  7 15   
Output
6

"""
import re
def longest_increasing_subsequence(arr,n):
    subsequence_length = [1]*len(arr)
    for i in range(0,n):
        j = i-1
        while(j>-1):
            if arr[j]<arr[i] and subsequence_length[j]+1>subsequence_length[i]:
                subsequence_length[i] = subsequence_length[j]+1
            j = j-1
    return max(subsequence_length)
    
def main():
    t = int(input())
    for i in range(0,t):
        n = int(input().strip(" "))
        arr_str = re.sub(r' +',' ',input()).split(" ")
        arr = []
        for item in arr_str:
            try:
                arr.append(int(item))
            except:
                pass
    print(longest_increasing_subsequence(arr,n))
if __name__ == '__main__':
    main()
    