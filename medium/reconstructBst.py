class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrder):
    return reconstructBstQuadraticTimeAndLinearSpace(preOrder)


"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def reconstructBstQuadraticTimeAndLinearSpace(preOrder):
    if len(preOrder) == 0:
        return

    current = preOrder[0]

    rightIndex = 1
    while rightIndex < len(preOrder) and preOrder[rightIndex] < current:
        rightIndex += 1

    leftNode = reconstructBstQuadraticTimeAndLinearSpace(preOrder[1:rightIndex])
    rightNode = reconstructBstQuadraticTimeAndLinearSpace(preOrder[rightIndex:])
    return BST(current, leftNode, rightNode)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def reconstructBstQuadraticLinearTimeAndLinearSpace(preOrder):
    currentIndex = 0

    def reconstructBstHelper(lower, upper, preOrder):
        nonlocal currentIndex

        if currentIndex == len(preOrder):
            return

        current = preOrder[currentIndex]
        if current < lower or current >= upper:
            return

        currentIndex += 1
        left = reconstructBstHelper(lower, current, preOrder)
        right = reconstructBstHelper(current, upper, preOrder)

        return BST(current, left, right)

    return reconstructBstHelper(float("-inf"), float("inf"), preOrder)