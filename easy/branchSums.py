class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return branchSumsRecursive(root, root.value)


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def branchSumsRecursive(node, currentSum, sums=None):
    if sums is None:
        sums = []

    if node.left is None and node.right is None:
        sums.append(currentSum)

    if node.left is not None:
        branchSumsRecursive(node.left, currentSum + node.left.value, sums)

    if node.right is not None:
        branchSumsRecursive(node.right, currentSum + node.right.value, sums)

    return sums


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def branchSumsIterative(root):
    stack = [(root, root.value)]
    sums = []

    while len(stack) > 0:
        node, sum = stack.pop()

        if node.left is None and node.right is None:
            sums.append(sum)

        if node.left is not None:
            stack.append((node.left, sum + node.left.value))

        if node.right is not None:
            stack.append((node.right, sum + node.right.value))

    sums.reverse()
    return sums