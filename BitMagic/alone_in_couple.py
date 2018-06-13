def alone_in_couple(arr,n):
    xor = 0
    for item in arr:
        xor = xor^item
    return xor
t = int(input())
for i in range(0,t):
    n = int(input())
    arr = [int(i) for i in input().strip().split(" ")];
    alone_in_couple(arr,n)