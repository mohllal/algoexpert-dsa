"""
O(n) time and O(1) space
n is the length of the input array
"""
def kadanesAlgorithm(array):
    localMaximum = 0
    globalMaximum = float("-inf")

    for i in range(len(array)):
        localMaximum = max(array[i], array[i] + localMaximum)
        globalMaximum = max(globalMaximum, localMaximum)

    return globalMaximum