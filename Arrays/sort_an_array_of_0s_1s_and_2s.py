# Write a program to sort an array of 0's,1's and 2's in ascending order.

# Input:
# The first line contains an integer 'T' denoting the total number of test cases. In each test cases, First line is number of elements in array 'N' and second its values.

# Output: 
# Print the sorted array of 0's, 1's and 2's.

# Constraints: 

# 1 <= T <= 100
# 1 <= N <= 100
# 0 <= arr[i] <= 2

# Example:

# Input :

# 2
# 5
# 0 2 1 2 0
# 3
# 0 1 0
 

# Output:

# 0 0 1 2 2
# 0 0 1


def sort_array(arr,n):
    count_arr = [0,0,0]
    for item in arr:
        count_arr[item] = count_arr[item] + 1
    return [0]*count_arr[0]+[1]*count_arr[1]+[2]*count_arr[2]

t = int(input())

for i in range(0,t):
    numbers = input().strip().split()
    n = int(numbers[0])

    arr = [int(x) for x in input().strip().split(" ")]
    result = sort_array(arr,n)
    for r in result:
        print(r," ",end="")
    print("\n")
