"""
url : https://practice.geeksforgeeks.org/problems/circle-of-strings/0

Given an array of strings A[ ], determine if the strings can be chained together to form a circle. A
string X can be chained together with another string Y if the last character of X is same as first
character of Y. If every string of the array can be chained, it will form a circle.

For eg for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"
 

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases
follow. 
The first line of each test case contains a positive integer N, denoting the size of the array.
The second line of each test case contains a N space seprated strings, denoting the elements of the
array A[ ].
 

Output
If chain can be formed, then print 1, else print 0.


Constraints
1 <= T <= 100
0 <   N  <= 30
0 <  A[i] <= 10
 

Examples 

Input
2
3
abc bcd cdf
4
ab bc cd da


Output
0
1

2
3
ceee eeece ddbc 
5
dedce cdcae debdc d abde
 
 """

from collections import defaultdict

def check_cycle(graph,visited,start_v,current_v):
    if len(visited) > len(graph):
        return False
    visited.append(current_v)
    for item in graph[current_v]:
        if start_v == item and len(visited) == len(graph):
            return True
        if item not in visited and check_cycle(graph,visited,start_v,item):
            return True
    visited.remove(current_v)
    return False

def isCyclic(n, graph):
    keys = list(graph.keys())
    visited = []
    if check_cycle(graph,visited,keys[0],keys[0]):
        return True
    return False

def convert_to_graph(strings):
    graph = defaultdict(list)
    for string in strings:
        graph[string[0]].append(string[-1])
    return graph

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        strings = input().strip(" ").split(" ")
        graph = convert_to_graph(strings)
        if isCyclic(n,graph):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()
     