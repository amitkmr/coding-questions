"""
https://practice.geeksforgeeks.org/problems/pass-the-semester/0
"""

INFINITE = 100000


def pass_semester(rem, array, time):
    if len(array) == 0:
        return INFINITE

    if marks <= 0:
        return 0
    if rem[marks] != None:
        return rem[marks]

    result = 10000

    for item in array:
        next_arr = array[:]
        next_arr.remove(item)
        result = min(result, item[0] + pass_semester(rem, next_arr, marks - item[1]))

    rem[marks] = result
    return rem[marks]


if __name__ == "__main__":
    for _ in range(int(input())):
        array_length, time, marks = list(map(int, input().split(" ")))
        array = []
        for i in range(array_length):
            array.append(tuple(map(int, input().split(" "))))
        rem = [None] * (marks + 1)
        result = pass_semester(rem, array, marks)
        if result <= time:
            print(f"YES {result}")
        else:
            print("NO")
