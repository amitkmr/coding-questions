"""
Write a function to print the depth first traversal for a undirected graph from a given source s.

Input:
The task is to complete the function DFS which takes 3 arguments an integer denoting the starting node (s) of the dfs travel , a  graph (g)  and an
array of visited nodes (vis)  which are initially all set to false .
There are multiple test cases. For each test case, this method will be called individually.
Output:
The function should print the depth first traversal for the graph from the given source.

Note : The expected output button always produces DFS starting from node 1.
Constraints:
1 <=T<= 100
1 <=Number of  edges<= 100
Example:
Input:
1
4
1 2 1 3 1 4 3 5

Output:
1 2 3 5 4    //dfs from node 1

There is  one test cases.  First line of each test case represent an integer N denoting no of edges and then in the next line N pairs of values a and
b are fed which denotes there is an edge from a to b .

"""
from collections import defaultdict

# Driver Program
def creategraph(n, arr, graph):
    i = 0
    while i<2*n:
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
        i+=2


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should print DFS Traversal
# Graph(graph) is a defaultict of type List
# Starting vertex (s) is 1
# Need not print new Line
# n is no of edges
# visit is a boolean array initialized to False
def dfs(n, visit, graph, s):
    print(s,end=" ")
    visit[s] = True

    for item in graph[s]:
        if visit[item] == False:
            dfs(n,visit,graph,item)
        else:
            continue



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(n, arr, graph)
        visit = [False]*(max(arr)+1)
        dfs(n, visit, graph, 1)
        print('')
# Contributed By: Harshit Sidhwa




