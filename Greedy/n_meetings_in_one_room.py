"""
There is one meeting room in Flipkart. There are n meetings in the form of (S [ i ], F [ i ]) where S [ i ] is start time of meeting i and F [ i ] is
finish time of meeting i

What is the maximum number of meetings that can be accommodated in the meeting room ?


Input:

The first line of input consists number of the test cases. The description of T test cases is as follows:

The first line consists of the size of the array, second line has the array containing the starting time of all the meetings each separated by a
space, i.e., S [ i ]. And the third line has the array containing the finishing time of all the meetings each separated by a space, i.e., F [ i ].

Output:

In each separate line print the order in which the meetings take place separated by a space.

Constraints:

1 <= T <= 70

1 <= N <= 100

1 <= S[ i ], F[ i ] <= 100000

Example:

Input:

2
6
1 3 0 5 8 5
2 4 6 7 9 9
8
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252

Output:

1 2 4 5
6 7 1
"""

def activity_selection(arr,n):
    arr = sorted(arr,key=lambda item:item[2])
    activities = []
    prev_time = -1
    for element in arr:
        if element[1] >= prev_time:
            activities.append(element[0])
            prev_time = element[2]

    for item in activities:
        print(item, end=" ")
    print()             
        

def main():
    t = int(input().strip())
    for i in range(0,t):
        n = int(input().strip())
        s_arr = [int(x) for x in input().strip().split(" ")]
        e_arr = [int(x) for x in input().strip().split(" ")]
        arr = []
        for j in range(0,n):
            arr.append((j+1,s_arr[j],e_arr[j]))
        activity_selection(arr,n)

if __name__ == '__main__':
    main()

