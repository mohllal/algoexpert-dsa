"""
O(n) time and O(1) space
n is the length of the input array
"""
def findThreeLargestNumbers(array):
    firstLargestNumber = max(array[0], array[1], array[2])
    thirdLargestNumber = min(array[0], array[1], array[2])
    secondLargestNumber = sum([array[0], array[1], array[2]]) - firstLargestNumber - thirdLargestNumber

    for i in range(3, len(array)):
        if array[i] > firstLargestNumber:
            thirdLargestNumber = secondLargestNumber
            secondLargestNumber = firstLargestNumber
            firstLargestNumber = array[i]
        elif array[i] > secondLargestNumber:
            thirdLargestNumber = secondLargestNumber
            secondLargestNumber = array[i]
        elif array[i] > thirdLargestNumber:
            thirdLargestNumber = array[i]

    return [thirdLargestNumber, secondLargestNumber, firstLargestNumber]