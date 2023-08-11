"""
O(n) time and O(1) space
n is the length of the input array
"""
def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        if array[right] == toMove:
            right -= 1
        elif array[left] != toMove:
            left += 1
        else:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1
    return array