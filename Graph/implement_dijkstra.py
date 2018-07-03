"""
url : https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

Given an adjacency matrix (graph), the task is to find the shortest distance of all the vertex's from the source vertex. You are required to complete the function dijkstra which takes 3 arguments. The first argument is the adjacency matrix (graph) , the second argument is the source vertex s and the third argument is V denoting the size of the matrix. The function prints  V space separated integers where i'th integer denotes the shortest distance of the i'th vertex from source vertex.

Input:
The first line of input contains an integer T denoting the no of test cases . Then T test cases follow .The first line of each test case contains an integer V denoting the size of the adjacency matrix  and in the next line are V space separated values of the matrix (graph) .The third line of each test case contains an integer denoting the source vertex s.

Output:
For each test case output will be V space separated integers where the ith integer denote the shortest distance of ith vertex from source vertex.

Constraints:
1<=T<=20 
1<=V<=20
0<=s 1<=graph[][]<=1000

Example:
Input
2
2
0 25 25 0
0
3
0 1 43 1 0 6 43 6 0
2

Output
0 25
7 6 0

"""

# Your code goes here
import heapq
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[c]
                c+=1
        s = int(input())
        dijkstra(matrix, n, s)
        print('')
# Contributed By: Harshit Sidhwa

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# The function prints V space separated integers where 
# the ith integer denote the shortest distance of ith vertex
# from source vertex

def parent(i):
    return (i-1)>>1;

def left(i):
    return (i<<1) + 1

def right(i):
    return (i<<1) + 2

def find_node(heap,index, node):
    if index >= len(heap):
        return -1
    if heap[index][0] == node[0] and heap[index][1] == node[1]:
        return index
    result = find_node(heap,left(index),node)
    if result !=-1:
        return result
    else:
        return find_node(heap,right(index),node)

def sift_up(heap,node,new_value):
    index = find_node(heap,0,node)
    heap[index] = (new_value,node[1])
    while(index!=0):
        if heap[parent(index)][0] > heap[index][0]:
            heap[parent(index)],heap[index] = heap[index],heap[parent(index)]
            index = parent(index)
        else:
            break
    

def print_arr(arr):
    for item in arr:
        print(item,end=" ")
    
def dijkstra(matrix, v, s):
    queue = []
    for i in range(v):
        queue.append((1000,i))
    distance = [1000]*v
    distance[s] = 0
    sift_up(queue,(1000,s),0)
    while(len(queue)>0):
        vertex = heapq.heappop(queue)[1]
        for i in range(v):
                new_distance = matrix[vertex][i]+distance[vertex]
                if distance[i] > new_distance:
                    sift_up(queue,(distance[i],i),new_distance)
                    distance[i] = new_distance
    print_arr(distance)

if __name__ == '__main__':
    main()
    
