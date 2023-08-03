class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    return nodeDepthsRecursive(root)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def nodeDepthsRecursive(root, depth=0):
    if root is None:
        return 0

    return (
        depth
        + nodeDepthsRecursive(root.left, depth+1)
        + nodeDepthsRecursive(root.right, depth+1)
    )


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def nodeDepthsIterative(root):
    depths = 0
    stack = [(root, 0)]

    while len(stack) > 0:
        node, depth = stack.pop()
        depths += depth

        if node.left is not None:
            stack.append((node.left, depth+1))

        if node.right is not None:
            stack.append((node.right, depth+1))

    return depths