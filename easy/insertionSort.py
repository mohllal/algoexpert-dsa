"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array
