#written 10.24.26
#binary search with a loop
def binarySearch(arr, low, high, x):
    mid = (low+high)//2
    while low <= high:
        if arr[mid] == x:
            return mid
        elif arr[mid] <x:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [1, 3,  8, 23, 54, 233, 454]
#binary search with recursion (better)
print(binarySearch(arr, 0, len(arr), 23))
def binarSearchRec(arr, low, high, x):
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binarSearchRec(arr, mid+1, high, x)
    else:
        return binarSearchRec(arr,low, mid-1,x)
    return -1
print(binarSearchRec(arr, 0, len(arr), 8))