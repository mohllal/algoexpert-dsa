"""
O(w*h) time and O(w*h) space
w is the width of the input array
h is the height of the input array
"""
def zigzagTraverse(array):
    row, height = 0, len(array) - 1
    column, width = 0, len(array[0]) - 1

    result = []
    down = True
    while row <= height and column <= width:
        result.append(array[row][column])

        if down:
            if row == height:
                column += 1
                down = False
            elif column == 0:
                row += 1
                down = False
            else:
                row += 1
                column -= 1
        else:
            if column == width:
                row += 1
                down = True
            elif row == 0:
                column += 1
                down = True
            else:
                column += 1
                row -= 1

    return result