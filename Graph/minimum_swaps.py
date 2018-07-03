"""
url : https://practice.geeksforgeeks.org/problems/minimum-swaps/1

Given an array of N distinct elementsA[ ], find the minimum number of swaps required to sort the array.
Your are required to complete the function which returns an integer denoting the minimum number of swaps, 
required to sort the array.

Examples:

Input : {4, 3, 2, 1}
Output : 2
Explanation : Swap index 0 with 3 and 1 with 2 to 
              form the sorted array {1, 2, 3, 4}.

Input : {1, 5, 4, 3, 2}
Output : 2

Input:
The first line of input contains an integer T denoting the no of test cases . 
Then T test cases follow . Each test case contains an integer N denoting the no of element of 
the array A[ ]. In the next line are N space separated values of the array A[ ] .

Output:
For each test case in a new line output will be an integer denoting  minimum umber of swaps that 
are  required to sort the array.

Constraints:
1<=T<=100
1<=N<=100
1<=A[] <=1000

Example(To be used only for expected output):
Input:
2
4
4 3 2 1
5
1 5 4 3 2
Output:
2
2

"""

from collections import defaultdict

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        minSwaps(arr, n)
# Contributed by: Harshit Sidhwa


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# function should return an integer denoting the minimum number of swap's


def count_swaps(graph,visited,current, count):
    if current in visited:
        return count-1
    else:
        visited.append(current)
        return count_swaps(graph,visited,graph[current],count + 1)

def create_graph(arr,n):
    graph = {}
    visited = []
    sorted_arr = sorted(arr)
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            graph[arr[i]] = sorted_arr[i]
        else:
            visited.append(arr[i])
    print(graph)
    return graph,visited


def minSwaps(arr, n):
    graph,visited = create_graph(arr,n)
    swaps = 0
    for item in arr:
        if item not in visited:
            swaps = swaps + count_swaps(graph,visited,item,0)
    print(swaps)

if __name__ == '__main__':
    main()
    