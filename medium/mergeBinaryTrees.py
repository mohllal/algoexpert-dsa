class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def mergeBinaryTrees(tree1, tree2):
    return mergeBinaryTreesAnotherLinearTimeAndLinearSpace(tree1, tree2)

"""
O(n) time O(n) space
n is the total number of nodes in the merged tree
"""
def mergeBinaryTreesLinearTimeAndLinearSpace(tree1, tree2):
    if tree1 is None and tree2 is None:
        return

    value1 = tree1.value if tree1 is not None else 0
    value2 = tree2.value if tree2 is not None else 0

    node = BinaryTree(value1 + value2)

    left1 = tree1.left if tree1 is not None else None
    left2 = tree2.left if tree2 is not None else None
    node.left = mergeBinaryTreesLinearTimeAndLinearSpace(left1, left2)

    right1 = tree1.right if tree1 is not None else None
    right2 = tree2.right if tree2 is not None else None
    node.right = mergeBinaryTreesLinearTimeAndLinearSpace(right1, right2)

    return node


"""
O(n) time O(h) space
n is the number of nodes in the smallest input tree
h is the height of the smallest input tree
"""
def mergeBinaryTreesAnotherLinearTimeAndLinearSpace(tree1, tree2):
    if tree1 is None:
        return tree2

    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTreesAnotherLinearTimeAndLinearSpace(tree1.left, tree2.left)
    tree1.right = mergeBinaryTreesAnotherLinearTimeAndLinearSpace(tree1.right, tree2.right)

    return tree1