"""
url : https://practice.geeksforgeeks.org/problems/box-stacking/1
You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and length l. You task is to create a stack of boxes
which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly
larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base.It is also allowable to
use multiple instances of the same type of box. You task is to complete the function maxHeight which returns the height of the highest possible stack
so formed.
Input:
The first line of input contains an integer T denoting the no of test cases then T test cases follow . Each test case contains an integer N denoting
the total no of boxes available. In the next line are 3*N space separated values denoting the height width and length of the N boxes.
Output:
For each test case in a new line output will be the highest possible stack height which could be formed.
Constraints:
1<=T<=100
1<=N<=100
1<=l,w,h<=100
Example (To be used for expected output) :
Input:
2
4
4 6 7 1 2 3 4 5 6 10 12 32
3
1 2 3 4 5 6 3 4 1
Output
60
15
"""

def max_height_boxes(boxes,x,y,rem):
    if rem[x][y] != -1:
        return rem[x][y] 
    
    max_height = 0
    for i in range(0,len(boxes)):
        box = boxes[i]
        x_height = 0
        y_height = 0
        z_height = 0
        
        if box[0] < x and box[1] < y or box[0] < y and box[1] < x:
            x_height = box[2] + max_height_boxes(boxes,box[0],box[1],rem)

        if box[0] < x and box[2] < y or box[0] < y and box[2] < x:
            y_height = box[1] + max_height_boxes(boxes,box[0],box[2],rem) 

        if box[1] < x and box[2] < y or box[1] < y and box[2] < x:
            z_height = box[0] + max_height_boxes(boxes,box[1],box[2],rem)

        max_height = max(max_height,x_height,y_height,z_height)
    rem[x][y] = max_height
    return max_height 
        
        
def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        arr = [int(x) for x in input().strip(" ").split(" ")]
        boxes = []
        for j in range(0,n):
            boxes.append((arr[3*j],arr[3*j+1],arr[3*j+2]))
        rem = []
        for j in range(0,101):
            rem.append([-1]*(101))
        print(max_height_boxes(boxes,100,100,rem))


if __name__ == '__main__':
    main()

    