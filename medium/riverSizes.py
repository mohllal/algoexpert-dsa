"""
O(r*c) time and O(r*c) space
r is the number of rows in the input matrix
c is the number of columns in the input matrix
"""
def riverSizes(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j] and matrix[i][j]:
                size = riverSizeStartingAtIndex(matrix, visited, i, j)
                sizes.append(size)

    return sizes


def getNeighbours(matrix, row, column):
    neighbours = []

    if column - 1 >= 0:
        neighbours.append([row, column - 1])

    if column + 1 < len(matrix[0]):
        neighbours.append([row, column + 1])

    if row - 1 >= 0:
        neighbours.append([row - 1, column])

    if row + 1 < len(matrix):
        neighbours.append([row + 1, column])

    return neighbours


def riverSizeStartingAtIndex(matrix, visited, row, column):
    visited[row][column] = True

    size = 1
    neighbours = getNeighbours(matrix, row, column)
    for cRow, cColumn in neighbours:
        if not visited[cRow][cColumn] and matrix[cRow][cColumn]:
            size += riverSizeStartingAtIndex(matrix, visited, cRow, cColumn)

    return size