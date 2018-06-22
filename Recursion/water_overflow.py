"""
https://practice.geeksforgeeks.org/problems/champagne-overflow/0

There is a stack of water glasses in a form of pascal triangle and a person wants to pour the water at the topmost glass, but the capacity of each glass is 1 unit . Overflow takes place in such a way that after 1 unit, 1/2 of remaining unit gets into bottom left glass and other half in bottom right glass.

Now the pours K units of water in the topmost glass and wants to know how much water is there in the jth glass of the ith row.

Assume that there are enough glasses in the triangle till no glass overflows. 

Input:   First line of the input contains an integer T denoting the number of test cases and each test case consists of three lines. First line contain an integer K, second line contains an integer i and third line contains an integer j.


Output: Corresponding to each test case output the remaining amount of water in jth cup of the ith row correct to 6 decimal places.


Constraints:

T<=20
K<=1000
i <= K
j<= K
                
Example:
Input:

1
3 
2
1

Output:
1

"""
def water_in_glass(k,i,j):
    if j>i or j <= 0:
        return 0
    if i == 1 and j==1:
        return k
    
    left_water = water_in_glass(k,i-1,j-1)
    right_water = water_in_glass(k,i-1,j)

    total_water = 0.0
    if left_water > 1:
        total_water = total_water + (left_water-1)/2
    
    if right_water > 1:
        total_water = total_water + (right_water-1)/2
    
    return total_water
    

def main():
    t = int(input())
    for i in range(0,t):
        k = int(input())
        i = int(input())
        j = int(input())
        over_flow_water = water_in_glass(k,i,j)
        if over_flow_water > 1:
            print(1.0)
        else:
            print(over_flow_water)

if __name__ == '__main__':
    main()
    