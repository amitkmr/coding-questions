"""
Given a collection of Intervals,merge all the overlapping Intervals.
For example:

Given [1,3], [2,6], [8,10], [15,18],

return [1,6], [8,10], [15,18].

Make sure the returned intervals are sorted.

 

Input:

The first line contains an integer T, depicting total number of test cases. 
Then following T lines contains an integer N depicting the number of Intervals and next line followed by the intervals starting and ending positions 'x' and 'y' respectively.


Output:

Print the intervals after overlapping in sorted manner.  There should be a newline at the end of output of every test case.

Constraints:

1 ≤ T ≤ 50
1 ≤ N ≤ 100
0 ≤ x ≤ y ≤ 100


Example:

Input
2
4
1 3 2 4 6 8 9 10
4
6 8 1 9 2 4 4 7

Output
1 4 6 8 9 10
1 9

"""

def merge_overlapping_interval(arr,n):
    arr = sorted(arr)

    prev = None
    result = []
    for item in arr:
        if prev == None:
            prev = item
            continue

        if item[0] <= prev[1]:
            prev = (prev[0],max(prev[1],item[1]))
        else:
            result.append(prev)
            prev = item
    result.append(prev)
    return result

def test():
    n = 4
    arr = [(1,1),(2,2),(6,8),(9,10)]
    print(merge_overlapping_interval(arr,n))
    arr = [(6,8),(1,9),(2,4),(4,7)]
    print(merge_overlapping_interval(arr,n))

def print_interval(arr):
    for item in arr:
        print(item[0],item[1],end=" ")
    print()

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        arr = []
        for j in range(n):
            arr.append((a[2*j],a[2*j+1]))
        print_interval(merge_overlapping_interval(arr,n))

if __name__ == '__main__':
    main()
    