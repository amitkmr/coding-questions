"""
Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that
a person can only work on a single activity at a time.
Note : The start time and end time of two activities may coincide.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases. First line is N number of activities then second
line contains N numbers which are starting time of activies.Third line contains N finishing time of activities.

Output:
For each test case, output a single number denoting maximum activites which can be performed in new line.

Constraints:
1<=T<=50
1<=N<=1000
1<=A[i]<=100

Example:
Input:
1
6
1 3 0 5 8 5
2 4 6 7 9 9

Output:
4
"""

def activity_selection(arr,n):
    arr = sorted(arr,key=lambda item:item[1])
    total_activity = 0
    prev_time = -1
    for element in arr:
        if element[0] >= prev_time:
            total_activity = total_activity + 1
            prev_time = element[1]
    return total_activity             
        

def main():
    t = int(input().strip())
    for i in range(0,t):
        n = int(input().strip())
        s_arr = [int(x) for x in input().strip().split(" ")]
        e_arr = [int(x) for x in input().strip().split(" ")]
        arr = []
        for j in range(0,n):
            arr.append((s_arr[j],e_arr[j]))
        print(activity_selection(arr,n))

if __name__ == '__main__':
    main()
    