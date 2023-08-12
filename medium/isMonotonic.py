def isMonotonic(array):
    return isMonotonicLinearTimeAndConstantSpace(array)

"""
O(n) time and O(1) space
n is the lenght of the input array
"""
def isMonotonicLinearTimeAndConstantSpace(array):
    decreasing = True
    increasing = True

    for i in range(0, len(array) - 1):
        if array[i] < array[i + 1]:
            decreasing = False

        if array[i] > array[i + 1]:
            increasing = False

    return decreasing or increasing