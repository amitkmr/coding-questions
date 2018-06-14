
def anagram(string1,string2):
    if sorted(string1) == sorted(string2):
        print("YES")
    else:
        print("NO")


t = int(input())

for i in range(0,t):
    string1 = input()
    string2 = input()
    anagram(string1,string2)