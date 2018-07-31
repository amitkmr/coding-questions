def parent(i):
    return int((i-1)/2)
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2


def heapify(arr,n,i):
    small = i

    if left(i) < n and arr[left(i)] < arr[i]:
        small = left(i)
    
    if right(i) < n and arr[right(i)] < arr[small]:
        small = right(i)

    # swap two elements
    if small != i:
        arr[small],arr[i] = arr[i],arr[small]
        heapify(arr,n,small)


def extract_min(arr):
    print(arr)
    n = len(arr)s
    item = arr[0]
    arr[0],arr[n-1] = arr[n-1],arr[0]
    arr.pop()
    heapify(arr,n-1,0)
    return item