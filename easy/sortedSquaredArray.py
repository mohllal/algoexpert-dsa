def sortedSquaredArray(array):
    return sortedSquaredArrayLogLinearTimeAndLinearSpace(array)


"""
O(nlog(n)) time and O(n) space
n is the length of the input array
"""
def sortedSquaredArrayLogLinearTimeAndLinearSpace(array):
    squares = [num**2 for num in array]
    squares.sort()
    return squares


"""
O(n) time and O(n) space
n is the length of the input array
"""
def sortedSquaredArrayLinearTimeAndLinearSpace(array):
    left = 0
    right = len(array) - 1
    squares = []

    while left <= right:
        leftSquared = array[left] ** 2
        rightSquared = array[right] ** 2

        if leftSquared > rightSquared:
            squares.append(leftSquared)
            left += 1
        else:
            squares.append(rightSquared)
            right -= 1

    squares.reverse()
    return squares
