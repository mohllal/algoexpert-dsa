class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
O(n) time and O(d) space
n is the number of nodes in the input tree
d is the depth of the input tree
"""
def sumBsts(tree):
    def sumBstsHelper(node):
        if node is None:
            return True, 0, 0, 0, float('inf'), float('-inf')

        isLeftBst, leftSum, leftTotal, leftSize, leftMin, leftMax = sumBstsHelper(node.left)
        isRightBst, rightSum, rightTotal, rightSize, rightMin, rightMax = sumBstsHelper(node.right)

        isCurrentBst = isLeftBst and isRightBst and node.value > leftMax and node.value <= rightMin
        currentMin = min(node.value, leftMin, rightMin)
        currentMax = max(node.value, leftMax, rightMax)

        currentTotal = leftTotal + rightTotal
        currentSum = 0
        currentSize = 0

        if isCurrentBst:
            currentSize = leftSize + rightSize + 1
            currentSum = leftSum + rightSum + node.value

            if currentSize == 3:
                currentTotal = currentSum

            if currentSize > 3:
                currentTotal += node.value

                if leftSize < 3:
                    currentTotal += leftSum

                if rightSize < 3:
                    currentTotal += rightSum

        return (
            isCurrentBst,
            currentSum,
            currentTotal,
            currentSize,
            currentMin,
            currentMax,
        )

    _, _, summation, _, _, _ = sumBstsHelper(tree)
    return summation
