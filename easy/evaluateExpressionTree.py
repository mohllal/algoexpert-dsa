class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    return postOrderTraversal(tree)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def postOrderTraversal(node):
    if node.left is None and node.right is None:
        return node.value

    if node.value == -1:
        return postOrderTraversal(node.left) + postOrderTraversal(node.right)
    elif node.value == -2:
        return postOrderTraversal(node.left) - postOrderTraversal(node.right)
    elif node.value == -3:
        return int(postOrderTraversal(node.left) / postOrderTraversal(node.right))
    else:
        return postOrderTraversal(node.left) * postOrderTraversal(node.right)
