def firstDuplicateValue(array):
    return firstDuplicateValueLinearTimeAndLinearSpace(array)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def firstDuplicateValueLinearTimeAndLinearSpace(array):
    unique = set()

    for number in array:
        if number in unique:
            return number
        unique.add(number)

    return -1


"""
O(n) time and O(1) space
n is the length of the input array
"""
def firstDuplicateValueLinearTimeAndConstantSpace(array):
    for i in range(len(array)):
        index = abs(array[i]) - 1

        if array[index] < 0:
            return abs(array[i])

        array[index] *= -1

    return -1