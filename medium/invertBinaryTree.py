class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    return invertBinaryTreeIterativeLinearTimeAndLinearSpace(tree)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def invertBinaryTreeIterativeLinearTimeAndLinearSpace(tree):
    stack = [tree]

    while len(stack) > 0:
        node = stack.pop()

        if node is None:
            continue

        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)

    return tree


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def invertBinaryTreeRecursiveLinearTimeAndLinearSpace(tree):
    if tree is None:
        return

    tree.left, tree.right = tree.right, tree.left

    invertBinaryTreeRecursiveLinearTimeAndLinearSpace(tree.left)
    invertBinaryTreeRecursiveLinearTimeAndLinearSpace(tree.right)

    return tree