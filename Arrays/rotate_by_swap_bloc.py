## This is array rotation using swap bloc algorith


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def rotate_left(arr, k, l, r):
    n = r - l + 1
    if n == k:
        return

    if n < k:
        return rotate_left(arr, k % n, l, r)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 3
    # left rotation by k
    rotate_left(arr, k)
