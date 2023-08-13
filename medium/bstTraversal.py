
def inOrderTraverse(tree, array):
    return inOrderTraverseRecursive(tree, array)


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def inOrderTraverseRecursive(node, array):
    if node is None:
        return

    inOrderTraverse(node.left, array)
    array.append(node.value)
    inOrderTraverse(node.right, array)
    return array


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def inOrderTraverseIterative(node, array):
    current = node
    stack = []

    while len(stack) > 0 or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            array.append(current.value)
            current = current.right

    return array


def preOrderTraverse(tree, array):
    return preOrderTraverseRecursive(tree, array)


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def preOrderTraverseRecursive(node, array):
    if node is None:
        return

    array.append(node.value)
    preOrderTraverse(node.left, array)
    preOrderTraverse(node.right, array)

    return array

"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def preOrderTraverseIterative(node, array):
    stack = [node]

    while len(stack) > 0:
        current = stack.pop()
        array.append(current.value)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return array


def postOrderTraverse(tree, array):
    return postOrderTraverseRecursive(tree, array)


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def postOrderTraverseRecursive(node, array):
    if node is None:
        return

    postOrderTraverse(node.left, array)
    postOrderTraverse(node.right, array)
    array.append(node.value)

    return array


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def postOrderTraverseIterative(node, array):
    stack = [node]

    while len(stack) > 0:
        current = stack.pop()
        array.append(current.value)

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

    array.reverse()
    return array