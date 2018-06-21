"""
url : https://practice.geeksforgeeks.org/problems/page-faults-in-lru/0

In operating systems that use paging for memory management, page replacement algorithm are needed to decide which page needs to be replaced when the
new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the
existing pages with a newly needed page.
Given a sequence of pages and memory capacity, your task is to find the number of page faults using Least Recently Used (LRU) Algorithm.
Input:
The first line of input contains an integer T denoting the number of test cases. Each test case contains n number of pages and next line contains
space seaprated sequence of pages. The following line consist of the capacity of the memory.
Note: Pages are referred in the order left to right from the array (i.e index 0 page is referred first then index 1 and so on). Memory is empty at
thestart .
Output:
Output the number of page faults.
Constraints:
1<=T<=100
1<=n<=1000
4<=capacity<=100
Example:
Input:
2
9
5 0 1 3 2 4 1 0 5
4
8
3 1 0 2 5 4 1 2
4
Output:
8
7

"""

def page_faults(arr,n,k):
    pages = []
    count = 0
    for item in arr:
        if item in pages:
            pages.remove(item)
            pages.append(item)
            continue
        else:
            pages.append(item)
            count = count + 1
        if len(pages) > k:
            pages.pop(0)
    print(count)
        

def main():
    t = int(input().strip())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip().split(" ")]
        k = int(input())
        page_faults(arr,n,k)

if __name__ == '__main__':
    main()

