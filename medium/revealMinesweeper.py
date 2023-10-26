"""
O(n*m) time and O(n*m) space
n is the rows number of the input board
m is the columns number of the input board
"""
def revealMinesweeper(board, row, column):
    if board[row][column] == "M":
        board[row][column] = "X"
        return board

    neighbours = getNeighbours(board, row, column)

    numOfAdjacentMines = 0
    for rNeighbour, cNeighbour in neighbours:
        if board[rNeighbour][cNeighbour] == "M":
            numOfAdjacentMines += 1

    board[row][column] = str(numOfAdjacentMines)

    if numOfAdjacentMines == 0:
        for rNeighbour, cNeighbour in neighbours:
            if board[rNeighbour][cNeighbour] == "H":
                revealMinesweeper(board, rNeighbour, cNeighbour)

    return board


def getNeighbours(board, row, column):
    neighbours = []

    if row - 1 >= 0:
        neighbours.append([row - 1, column])

    if row + 1 < len(board):
        neighbours.append([row + 1, column])

    if column - 1 >= 0:
        neighbours.append([row, column - 1])

    if column + 1 < len(board[0]):
        neighbours.append([row, column + 1])

    if row + 1 < len(board) and column + 1 < len(board[0]):
        neighbours.append([row + 1, column + 1])

    if row + 1 < len(board) and column - 1 >= 0:
        neighbours.append([row + 1, column - 1])

    if row - 1 >= 0 and column - 1 >= 0:
        neighbours.append([row - 1, column - 1])

    if row - 1 >= 0 and column + 1 < len(board[0]):
        neighbours.append([row - 1, column + 1])

    return neighbours