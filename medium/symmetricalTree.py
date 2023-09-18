class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return symmetricalTreeLinearTimeAndLinearSpace(tree)


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def symmetricalTreeLinearTimeAndLinearSpace(tree):
    stack1 = [tree.left]
    stack2 = [tree.right]

    while len(stack1) > 0 and len(stack2) > 0:
        node1 = stack1.pop()
        node2 = stack2.pop()

        if node1 is None and node2 is None:
            continue

        if node1 is None or node2 is None:
            return False

        if node1.value != node2.value:
            return False

        stack1.append(node1.right)
        stack2.append(node2.left)

        stack1.append(node1.left)
        stack2.append(node2.right)

    if len(stack1) != 0 or len(stack2) != 0:
        return False

    return True


"""
O(n) time and O(h) space
n is the number of nodes in the input tree
h is the height of the input tree
"""
def symmetricalTreeAnotherLinearTimeAndLinearSpace(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    return (
        left.value == right.value and
        symmetricalTreeAnotherLinearTimeAndLinearSpace(left.left, right.right) and
        symmetricalTreeAnotherLinearTimeAndLinearSpace(left.right, right.left)
    )