class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def heightBalancedBinaryTree(tree):
    return heightBalancedBinaryTreeLinearTimeAndLinearSpace(tree)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def heightBalancedBinaryTreeLinearTimeAndLinearSpace(tree):
    balanced = True

    def heightBalancedBinaryTreeHelper(tree):
        nonlocal balanced

        if tree is None:
            return 0

        left = heightBalancedBinaryTreeHelper(tree.left)
        right = heightBalancedBinaryTreeHelper(tree.right)

        balanced &= abs(left - right) <= 1

        return 1 + max(left, right)

    heightBalancedBinaryTreeHelper(tree)
    return balanced


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def heightBalancedBinaryTreeAnotherLinearTimeAndLinearSpace(tree):
    def heightBalancedBinaryTreeHelper(tree):
        if tree is None:
            return True, 0

        leftTreeBalanced, leftTreeHeight = heightBalancedBinaryTreeHelper(tree.left)
        rightTreeBalanced, rightTreeHeight = heightBalancedBinaryTreeHelper(tree.right)

        if not leftTreeBalanced or not rightTreeBalanced:
            return False, -1

        if abs(leftTreeHeight - rightTreeHeight) <= 1:
            return True, 1 + max(leftTreeHeight, rightTreeHeight)
        else:
            return False, -1

    balanced, _ = heightBalancedBinaryTreeHelper(tree)
    return balanced