"""
O(n) time and O(n) space
n is the total number of elements in the input array
"""
def spiralTraverse(array):
    output = []
    rows = len(array)
    columns = len(array[0])

    rStart, rEnd = 0, rows - 1
    cStart, cEnd = 0, columns - 1
    while rStart <= rEnd and cStart <= cEnd:
        rectangleTraverse(rStart, rEnd, cStart, cEnd, array, output)

        rStart += 1
        rEnd -= 1

        cStart += 1
        cEnd -= 1

    return output


"""
O(r+c) time and O(1) space
r is the number of rows in the input array
c is the number of columns in the input array
"""
def rectangleTraverse(rStart, rEnd, cStart, cEnd, array, output):
    for column in range(cStart, cEnd + 1):
        output.append(array[rStart][column])

    for row in range(rStart + 1, rEnd + 1):
        output.append(array[row][cEnd])

    if rEnd != rStart:
        for column in reversed(range(cStart, cEnd)):
            output.append(array[rEnd][column])

    if cEnd != cStart:
        for row in reversed(range(rStart + 1, rEnd)):
            output.append(array[row][cStart])