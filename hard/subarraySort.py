def subarraySort(array):
    return subarraySortLinearTimeAndLinearSpace(array)


"""
O(n) time and O(1) space
n is the length of the input array
"""
def subarraySortLinearTimeAndLinearSpace(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        if isOutOfOrder(array, i):
            minOutOfOrder = min(minOutOfOrder, array[i])
            maxOutOfOrder = max(maxOutOfOrder, array[i])

    if minOutOfOrder == float("inf") and maxOutOfOrder == float("-inf"):
        return [-1, -1]

    subArrayLeft = 0
    while subArrayLeft < len(array) and array[subArrayLeft] <= minOutOfOrder:
        subArrayLeft += 1

    subArrayRight = len(array) - 1
    while subArrayRight >= 0 and array[subArrayRight] >= maxOutOfOrder:
        subArrayRight -= 1

    return [subArrayLeft, subArrayRight]


def isOutOfOrder(array, index):
    if index == 0:
        return array[index] > array[index + 1]
    elif index == len(array) - 1:
        return array[index] < array[index - 1]
    else:
        return array[index] < array[index - 1] or array[index] > array[index + 1]