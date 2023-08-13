class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstRecursive(tree)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def validateBstRecursive(node, min=float("-inf"), max=float("inf")):
    if node is None:
        return True

    if not (node.value >= min and node.value < max):
        return False

    isLeftBST = validateBstRecursive(node.left, min, node.value)
    isRightBST = validateBstRecursive(node.right, node.value, max)

    return isLeftBST and isRightBST