arr = [1, 3, 3, 4, 5, 6, 7, 8]

def binary_search(arr, target):
    L, R = 0, len(arr) -1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid - 1
    return -1