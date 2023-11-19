def sameBsts(arrayOne, arrayTwo):
    return sameBstsQuadraticTimeAndQuadraticSpace(arrayOne, arrayTwo)

"""
O(n^2) time and O(n^2) space
n is the longest input array
"""
def sameBstsQuadraticTimeAndQuadraticSpace(arrayOne, arrayTwo):
    def sameBstsHelper(arrayOne, arrayTwo):
        if len(arrayOne) != len(arrayTwo):
            return False

        if arrayOne == arrayTwo:
            return True

        if arrayOne[0] != arrayTwo[0]:
            return False

        leftOne, rightOne = partitionArray(arrayOne, arrayOne[0])
        leftTwo, rightTwo = partitionArray(arrayTwo, arrayTwo[0])

        return sameBstsHelper(leftOne, leftTwo) and sameBstsHelper(rightOne, rightTwo)

    return sameBstsHelper(arrayOne, arrayTwo)


def partitionArray(array, pivot):
    left = [array[i] for i in range(1, len(array)) if array[i] < pivot]
    right = [array[i] for i in range(1, len(array)) if array[i] >= pivot]

    return left, right
