class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
O(n) time and O(h) space
n is the number of nodes in the input ree
h is the height of the input tree
"""
def binaryTreeDiameter(tree):
    diameter = float("-inf")

    def binaryTreeDiameterHelper(tree):
        nonlocal diameter

        if tree is None:
            return 0

        left = binaryTreeDiameterHelper(tree.left)
        right = binaryTreeDiameterHelper(tree.right)

        diameter = max(left + right, diameter)

        return 1 + max(left, right)

    binaryTreeDiameterHelper(tree)
    return diameter