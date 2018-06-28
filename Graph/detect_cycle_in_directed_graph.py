"""
url : https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

Given a directed graph  your task is to complete the method isCycle  to detect if there is a cycle in the graph or not. You should not read any input from stdin/console.
There are multiple test cases. For each test case, this method will be called individually.
 

Input (only to be used for Expected Output):
The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of two lines. 
Description of  test cases is as follows:
The First line of each test case contains two integers 'N' and 'M'  which denotes the no of vertices and no of edges respectively.
The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is an unidirected  edge from u to v .

Output:
The method should return true if there is a cycle else it should return false.

Constraints:
1 <=T<= 100
1<=N,M<=100
0 <=u,v<= N-1

Example:
Input:
2
2 2
0 1 0 0
4 3
0 1 1 2 2 3

Output:
1
0

"""
from collections import defaultdict
# Driver Program
def creategraph(e,n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

def main():
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e,n, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices

def check_cycle(graph,visited,s):
    if visited[s] == True:
        return True
    visited[s] = True
    for item in graph[s]:
        if check_cycle(graph,visited,item):
            return True
    visited[s] = False
    return False

def isCyclic(n, graph):
    for i in range(n):
        visited = [False]*(n)
        if check_cycle(graph,visited,i):
            return True
    return False
if __name__ == '__main__':
    main()
    