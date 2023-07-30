"""
O(nlog(n)) time and O(1) space
n is the length of the input array
"""
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        return compareRowsHeights(blueShirtHeights, redShirtHeights)
    elif blueShirtHeights[0] > redShirtHeights[0]:
        return compareRowsHeights(redShirtHeights, blueShirtHeights)
    else:
        return False


"""
O(n) time and O(1) space
n is the length of the input array
"""
def compareRowsHeights(frontRowHeights, backRowHeights):
    for i in range(0, len(backRowHeights)):
        if backRowHeights[i] <= frontRowHeights[i]:
            return False
    return True