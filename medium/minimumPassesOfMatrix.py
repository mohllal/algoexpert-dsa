from collections import deque

"""
O(r*c) time and O(r*c) space
r is the number of rows in the input matrix
c is the number of columns in the input matrix
"""
def minimumPassesOfMatrix(matrix):
    positives = getPositives(matrix)
    positivesQueue = deque(positives)

    passes = 0
    while len(positivesQueue) > 0:
        currentPositivesCount = len(positivesQueue)

        while currentPositivesCount > 0:
            cRow, cColumn = positivesQueue.popleft()

            neighbours = getNeighbours(matrix, cRow, cColumn)
            for nRow, nColumn in neighbours:
                if matrix[nRow][nColumn] < 0:
                    matrix[nRow][nColumn] *= -1
                    positivesQueue.append([nRow, nColumn])

            currentPositivesCount -= 1

        passes += 1

    return passes - 1 if not containsNegative(matrix) else -1


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


def getPositives(matrix):
    positives = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                positives.append([i, j])

    return positives


def containsNegative(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                return True

    return False