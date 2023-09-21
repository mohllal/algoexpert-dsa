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
def splitBinaryTree(tree):
    treeSum = binaryTreeSum(tree)

    splittable = False
    if treeSum % 2 == 0:
        splittable = hasTreeWithSum(tree, treeSum // 2)

    return treeSum // 2 if splittable else 0

def binaryTreeSum(tree):
    if tree is None:
        return 0

    return tree.value + binaryTreeSum(tree.left) + binaryTreeSum(tree.right)

def hasTreeWithSum(tree, target):
    splittable = False

    def hasTreeWithSumHelper(tree, target):
        nonlocal splittable

        if tree is None or splittable:
            return 0

        left = hasTreeWithSumHelper(tree.left, target)
        right = hasTreeWithSumHelper(tree.right, target)

        current = tree.value + left + right
        splittable |= current == target

        return current

    hasTreeWithSumHelper(tree, target)
    return splittable