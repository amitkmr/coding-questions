"""
url :https://practice.geeksforgeeks.org/problems/topological-sort/1

Given a directed graph you need to complete the function topoSort which returns an array having the topologically sorted elements of the array and
takes two arguments . The first argument is the Graph graph represented as adjacency list and the second is the number of vertices N .

Note : There can be multiple topological sorts of a Graph.  The driver program that calls your function doesn't match your output element by element,
but checks whether the output produced by your function is a valid topological sort or not.
Input:
The first line of input takes the no of test cases then T test cases follow . Each test case contains two lines . The first  line of each test
case  contains two integers E and N representing no of edges and the no of vertices . Then in the next line are E  pairs of integers u v representing
an edge from u to v in the graph.
Output:
For each test case output will be 1 if the topological sort is done correctly else it will be 0 .
Constraints:
1<=T<=50
1<=E,N<=50
0<=u,v

Example:

Input
1
6 6
5 0 5 2 2 3 4 0 4 1 1 3
Output
1
"""

from collections import defaultdict
# Driver Program
def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2

def main():
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        # print res
        valid=True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i+1, N):
                    if res[k]==graph[res[i]][j]:
                        n-=1
            # print n
            if n!=0:
                valid=False
                break
        if valid:
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges

def dfs(n,visit, graph, s,result):
    visit[s] = True
    for item in graph[s]:
        if visit[item] == False:
            dfs(n,visit,graph,item,result)
        else:
            continue
    result.append(s)

def topoSort(n, graph):
    visit = [False]*(n)
    result = []
    for i in range(n):
        if visit[i] == False:
            dfs(n,visit,graph,i,result)
    print(result)
    return result[::-1]
if __name__ == '__main__':
    main()
    