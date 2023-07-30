"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array