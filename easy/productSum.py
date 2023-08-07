def productSum(array):
    return productSumRecursive(array)


"""
O(n) time O(n) space
n is the number of elements in the input array including sub-elements
"""
def productSumRecursive(array, index=0, depth=1):
    if index >= len(array):
        return 0

    if type(array[index]) is list:
        array[index] = (depth + 1) * productSumRecursive(array[index], 0, depth+1)

    return array[index] + productSumRecursive(array, index+1, depth)


"""
O(n) time O(d) space
n is the number of elements in the input array including sub-elements
d is the depth of the deepest special array
"""
def productSumAnotherRecursive(array, depth=1):
    sum = 0
    for index in range(0, len(array)):
        if type(array[index]) is list:
            array[index] = (depth + 1) * productSumAnotherRecursive(array[index], depth+1)
        sum += array[index]

    return sum