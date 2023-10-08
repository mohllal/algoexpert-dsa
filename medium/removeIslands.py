"""
O(r*c) time and O(r*c) space
r is the number of rows in the input matrix
c is the number of columns in the input matrix
"""
def removeIslands(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    fRow, eRow = 0, len(matrix) - 1
    for i in range(len(matrix[0])):
        if matrix[fRow][i] and not visited[fRow][i]:
            visitBorderedIslands(matrix, visited, fRow, i)

        if matrix[eRow][i] and not visited[eRow][i]:
            visitBorderedIslands(matrix, visited, eRow, i)

    fColumn, eColumn = 0, len(matrix[0]) - 1
    for i in range(len(matrix)):
        if matrix[i][fColumn] and not visited[i][fColumn]:
            visitBorderedIslands(matrix, visited, i, fColumn)

        if matrix[i][eColumn] and not visited[i][eColumn]:
            visitBorderedIslands(matrix, visited, i, eColumn)

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] and not visited[i][j]:
                matrix[i][j] = 0
    return matrix


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


def visitBorderedIslands(matrix, visited, row, column):
    visited[row][column] = True

    neighbours = getNeighbours(matrix, row, column)
    for cRow, cColumn in neighbours:
        if not visited[cRow][cColumn] and matrix[cRow][cColumn]:
            visitBorderedIslands(matrix, visited, cRow, cColumn)