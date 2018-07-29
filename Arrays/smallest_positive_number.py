"""
https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0

You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in O(n) time using constant extra space.

Input:
First line consists of T test cases. First line of every test case consists of N, denoting the number of elements in array. Second line of every test case consists of elements in array.

Output:
Single line output, print the smallest positive number missing.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
5
1 2 3 4 5
5
0 -10 1  -20
Output:
6
2

"""

def parent(i):
    return int((i-1)/2)
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2


def heapify(arr,n,i):
    small = i

    if left(i) < n and arr[left(i)] < arr[i]:
        small = left(i)
    
    if right(i) < n and arr[right(i)] < arr[small]:
        small = right(i)

    # swap two elements
    if small != i:
        arr[small],arr[i] = arr[i],arr[small]
        heapify(arr,n,small)


def extract_min(arr):
    print(arr)
    n = len(arr)
    item = arr[0]
    arr[0],arr[n-1] = arr[n-1],arr[0]
    arr.pop()
    heapify(arr,n-1,0)
    return item

def smallest_positive(arr,n):
    
    # for i in range(n):
    #     if arr[i] < 0:
    #         arr[i] = 100000000
    
    for i in range(int(n/2),-1,-1):
        heapify(arr,n,i)
    prev = None
    while(len(arr)>0):
        item = extract_min(arr)
        if item < 0:
            continue
        if item != 1:
            return 1
        if prev == None or prev+1 == item:
            prev = item
            continue
        else:
            return prev+1
    return prev + 1

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(smallest_positive(arr,n))


if __name__ == '__main__':
    main()
    