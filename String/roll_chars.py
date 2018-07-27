"""
https://practice.geeksforgeeks.org/problems/roll-the-characters-of-a-string/0

We are given a string s and an array roll where roll[i] represents rolling first roll[i] characters in string. We need to apply every roll[i] on string and output final string. Rolling means increasing ASCII value of character, like rolling ‘z’ would result in ‘a’, rolling ‘b’ would result in ‘c’, etc.

Input : s = "bca"
roll[] = {1, 2, 3}
Output : eeb

Explanation :
arr[0] = 1 means roll first character of string -> cca
arr[1] = 2 means roll first two characters of string -> dda
arr[2] = 3 means roll first three characters of string -> eeb
So final ans is "eeb"
Input:
First line consist of T test cases. First line of every test case consists of N. Second and third line consists of String and Array of N size, respectively.

Output:
Single line output, print the modified String.

Constraints:
1<=T<=100
1<=N<=1000

Example:
Input:
1
3
bca
1 2 3
Output:
eeb

"""
    
    


def roll_string(string,rolls):
	rotated = [0]*len(string)
	for item in rolls:
    		rotated[item-1]+=1
	for j in range(len(rotated)-2,-1,-1):
    		rotated[j] = rotated[j+1]+rotated[j]

	for j in range(0,len(string)):
		string = string[:j]+chr(ord('a')+(ord(string[j])-ord('a')+rotated[j])%26)+string[j+1:]
	print(string)

def main():
	t = int(input())
	for i in range(t):
		n = int(input())
		string = input()
		arr = list(map(int,input().split()))
		roll_string(string,arr)
	
if __name__ == '__main__':
	main()
