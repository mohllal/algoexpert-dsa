def searchInSortedMatrix(matrix, target):
    return searchInSortedMatrixLinearTimeAndConstantSpace(matrix, target)


"""
O(nlog(m)) time and O(1) space
n is the number of rows in the input matrix
m is the number of columns in the input matrix
"""
def searchInSortedMatrixLogLinearTimeAndConstantSpace(matrix, target):
    for row in range(0, len(matrix)):
        column = binarySearch(matrix[row], target)

        if column != -1:
            return [row, column]

    return [-1, -1]


def binarySearch(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid

    return -1


"""
O(n+m) time and O(1) space
n is the number of rows in the input matrix
m is the number of columns in the input matrix
"""
def searchInSortedMatrixLinearTimeAndConstantSpace(matrix, target):
    row = 0
    column = len(matrix[0]) - 1

    while row < len(matrix) and column >= 0:
        if matrix[row][column] < target:
            row += 1
        elif matrix[row][column] > target:
            column -= 1
        else:
            return [row, column]

    return [-1, -1]