# Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. The rightmost element is always a leader. 

# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N denoting the size of array.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

# Output:
# Print all the leaders.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 0 <= A[i]<=100

# Example:
# Input:
# 2
# 6
# 16 17 4 3 5 2
# 5
# 1 2 3 4 0
# Output:
# 17 5 2
# 4 0

def leaders_in_an_array(arr,n):
    reverse_arr = arr[::-1]

    result = []
    max_sofar = -1 
    for item in reverse_arr:
        if item > max_sofar : 
            result.append(item)
            max_sofar = item
    for item in result[::-1]:
        print(item, end=" ")
    print()

t = int(input())

for i in range(0,t):
    numbers = input().strip().split()
    n = int(numbers[0])

    arr = [int(x) for x in input().strip().split(" ")]
    leaders_in_an_array(arr,n)