def binarySearch(array, target):
    return binarySearchRecursive(array, target, 0, len(array) - 1)


"""
O(log(n)) time and O(log(n)) space
n is the length of the input array
"""
def binarySearchRecursive(array, target, low, high):
    if high >= low:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binarySearchRecursive(array, target, low, mid - 1)
        else:
            return binarySearchRecursive(array, target, mid + 1, high)
    else:
        return -1


"""
O(log(n)) time and O(1) space
n is the length of the input array
"""
def binarySearchIterative(array, target):
    low = 0
    high = len(array) - 1

    while high >= low:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1