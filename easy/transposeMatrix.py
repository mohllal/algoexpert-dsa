def transposeMatrix(matrix):
    return transposeMatrixQuadraticTimeAndQuadraticSpace(matrix)


"""
O(n*m) time and O(n*m) space
n is the number of rows
m is the number of columns per row
"""
def transposeMatrixQuadraticTimeAndQuadraticSpace(matrix):
    transpose = []
    for j in range(0, len(matrix[0])):
        row = []
        for i in range(0, len(matrix)):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose


"""
O(n*m) time and O(n*m) space
n is the number of rows
m is the number of columns per row
"""
def transposeMatrixAnotherQuadraticTimeAndQuadraticSpace(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transpose = [[None] * n for _ in range(0, m)]

    for i in range(0, n):
        for j in range(0, m):
            transpose[j][i] = matrix[i][j]
    return transpose