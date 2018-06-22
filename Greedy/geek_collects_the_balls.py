"""

There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets n both roads are kept in
such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower
number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help
Geek to collect the maximum number of balls.

Input:
The first line of input contains T denoting the number of test cases. The first line of each test case contains two integers N and M, denoting the
number of buckets on road1 and road2 respectively. 2nd line of each test case contains N integers, number of balls in buckets on the first road.
3rd line of each test case contains M integers, number of balls in buckets on the second road.

Output:
For each test case output a single line containing the maximum possible balls that Geek can collect.

Constraints:
1<= T <= 1000
1<= N <= 10^3
1<= M <=10^3
0<= A[i],B[i]<=10^6

Example:
Input:
1
5 5
1 4 5 6 8
2 3 4 6 9

Output:
29
"""
def lastIndexOf(arr,item):
    return len(arr) - 1 - arr[::-1].index(item)

def intersection(arr1,arr2):
    return [x for x in arr1 if x in arr2]

def collect_balls(arr1,arr2,n):
    common_arr = intersection(arr1,arr2)
    sum_arr = 0
    while(len(common_arr)>0):
        common_number = common_arr.pop(0)
        index1 = lastIndexOf(arr1,common_number)
        index2 = lastIndexOf(arr2,common_number)
        if sum(arr1[:index1]) > sum(arr2[:index2]):
            sum_arr = sum_arr + sum(arr1[:index1])
        else:
            sum_arr = sum_arr + sum(arr2[:index2])
        arr1 = arr1[index1:]
        arr2 = arr2[index2:]

    if sum(arr1) > sum(arr2):
        sum_arr = sum_arr + sum(arr1)
    else:
        sum_arr = sum_arr + sum(arr2)

    return sum_arr


def main():
    t = int(input().strip())
    for i in range(0,t):
        numbers = input().replace("  "," ").strip(" ").split(" ")
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        arr1 = [int(x) for x in input().split(" ")]
        arr2 = [int(x) for x in input().split(" ")]
        print(collect_balls(arr1,arr2,n1))

if __name__ == '__main__':
    main()
    