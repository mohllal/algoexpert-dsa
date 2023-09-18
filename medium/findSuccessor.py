class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    return findSuccessorLinearTimeAndLinearSpace(tree, node)


"""
O(n) time and O(n) space
n is the number of nodes in the input array
"""
def findSuccessorLinearTimeAndLinearSpace(tree, node):
    inOrder = []
    inOrderTraversal(tree, inOrder)

    for i in range(0, len(inOrder) - 1):
        if inOrder[i] == node:
            return inOrder[i + 1]

    return None


def inOrderTraversal(tree, inOrder):
    if tree is None:
        return

    inOrderTraversal(tree.left, inOrder)
    inOrder.append(tree)
    inOrderTraversal(tree.right, inOrder)


"""
O(h) time and O(1) space
h is the height of the input tree
"""
def findSuccessorLinearTimeAndConstantSpace(tree, node):
    if node.right is not None:
        return findLeftmostChild(node.right)

    return findRightmostParent(node)


def findLeftmostChild(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def findRightmostParent(node):
    current = node

    while current.parent is not None and current.parent.right == current:
        current = current.parent

    return current.parent