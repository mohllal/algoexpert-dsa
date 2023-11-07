def largestRange(array):
    return largestRangeLogLinearTimeAndConstantSpace(array)

"""
O(nlog(n)) time O(1) space
n is the length of the input array
"""
def largestRangeLogLinearTimeAndConstantSpace(array):
    array.sort()

    result = []
    rangeStart = array[0]
    rangeEnd = array[0]
    rangeLength = 1
    longestLength = 0
    for i in range(1, len(array)):
        if array[i] == array[i - 1] + 1:
            rangeEnd = array[i]
            rangeLength += 1
        elif array[i] == array[i - 1]:
            rangeEnd = array[i]
        else:
            if rangeLength > longestLength:
                longestLength = rangeLength
                result = [rangeStart, rangeEnd]

            rangeLength = 1
            rangeStart = array[i]
            rangeEnd = array[i]

    if rangeLength > longestLength:
        result = [rangeStart, rangeEnd]

    return result


"""
O(n) time and O(n) space
n is the length of the input array
"""
def largestRangeLinearTimeAndLinearSpace(array):
    presence = {num: False for num in array}

    result = []
    longestLength = 0
    for num in array:
        if presence[num]:
            continue

        rangeLength = 1

        right = num
        while right in presence:
            presence[right] = True
            right += 1
            rangeLength += 1

        left = num
        while left in presence:
            presence[left] = True
            left -= 1
            rangeLength += 1

        if rangeLength > longestLength:
            longestLength = rangeLength
            result = [left + 1, right - 1]

    return result