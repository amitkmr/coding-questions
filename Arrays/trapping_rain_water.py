# Given n non-negative integers in array representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# For example:
# Input:
# 3
# 2 0 2
# Output:
# 2
# Structure is like below
# |  |
# |_|
# We can trap 2 units of water in the middle gap.

# Below is another example.



# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.
# Each test case contains an integer N followed by N numbers to be stored in array.

# Output:
# Print trap units of water in the middle gap.

# Constraints:
# 1<=T<=100
# 3<=N<=100
# 0<=Arr[i]<10

# Example:
# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9

# Output:
# 10
# 0

def trapping_rain_water(arr,n):
    stack = []

    water_quantity = 0
    columns_area = 0
    for i in range(0,n):
        if len(stack) == 0:
            stack.append(i)
            continue
        
        while(len(stack)>1 and arr[stack[len(stack)-1]]<arr[i]):
            columns_area = columns_area + arr[stack[len(stack)-1]]
            del(stack[len(stack)-1])
        if len(stack) == 1 and arr[stack[len(stack)-1]]<arr[i]:
            water_quantity = water_quantity + (i-stack[0]- 1)*arr[stack[0]]
            del(stack[0])
        stack.append(i)
    
    for i in range(0,len(stack)-1):
        water_quantity = water_quantity + arr[stack[len(stack)-1-i]] * (stack[len(stack)-1-i]-stack[len(stack)-2-i]-1)

    return water_quantity - columns_area

t = int(input())

for i in range(0,t):
    n = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    print(trapping_rain_water(arr,n))

