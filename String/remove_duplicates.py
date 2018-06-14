

def remove_duplicates(string):
    map = {}
    for c in string:
        map[c] = 1

    result = ""

    for c in string:
        if map[c] == 1:
            result = result + c
            map[c] = 0
    print(result) 
        
    

t = int(input())

for i in range(0,t):
    string = input()
    remove_duplicates(string)