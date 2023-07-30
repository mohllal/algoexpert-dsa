"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def selectionSort(array):
    for i in range(0, len(array)):
        minimumIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimumIndex]:
                minimumIndex = j

        array[i], array[minimumIndex] = array[minimumIndex], array[i]

    return array