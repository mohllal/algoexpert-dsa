"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def countSquares(points):
    squares = 0
    registry = set([tuple(point) for point in points])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            thirdPoint, fourthPoint = findSquareVertices(points[i], points[j])

            if thirdPoint in registry and fourthPoint in registry:
                squares += 1

    return squares // 2

def findSquareVertices(firstPoint, secondPoint):
    firstPointX, firstPointY = firstPoint
    secondPointX, secondPointY = secondPoint

    midPointX = (firstPointX + secondPointX) / 2
    midPointY = (firstPointY + secondPointY) / 2

    # vector for the first point to the second point
    vector = (secondPointX - firstPointX, secondPointY - firstPointY)

    # vector that is perpendicular to the previous vector
    pVector = (-vector[1], vector[0])

    thirdPoint = (midPointX + 0.5 * pVector[0], midPointY + 0.5 * pVector[1])
    fourthPoint = (midPointX - 0.5 * pVector[0], midPointY - 0.5 * pVector[1])
    return thirdPoint, fourthPoint
