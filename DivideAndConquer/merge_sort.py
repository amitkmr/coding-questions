"""
The task is to complete merge() function which is used to implement Merge Sort.

Input:
First line of the input denotes number of test cases 'T'. First line of the test case is the size of array and second line consists of array elements.


Output:
Sorted array in increasing order is displayed to the user.


Constraints:
1 <=T<= 50
1 <=N<= 1000
1 <=arr[i]<= 1000


Example:

Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1

Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10

"""

def merge(arr,p,mid,r):
    
    temp = arr[:]
    q = mid + 1
    k = p-1

    while(k<r):
        k = k + 1
        if p<=mid and q<=r and temp[p]<=temp[q]:
            arr[k] = temp[p]
            p = p + 1
            continue
        if q<=r and p<=mid and temp[q]<=temp[p]:
            arr[k] = temp[q]
            q = q + 1
            continue
        
        if q > r:
            arr[k] = temp[p]
            p = p + 1
            continue
        
        if p > mid:
            arr[k] = temp[q]
            q = q + 1
    


def merge_sort(arr,p,r):
    if (p>=r):
        return
    mid = int((p+r)/2)
    merge_sort(arr,p,mid)
    merge_sort(arr,mid+1,r)
    merge(arr,p,mid,r)

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    merge_sort(arr,0,n-1)
    print(" ".join([str(x) for x in arr]))