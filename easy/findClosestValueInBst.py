class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    return findClosestValueInBstLinearRecursive(tree, target, float("inf"))


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def findClosestValueInBstLinearRecursive(node, target, closest):
    if node is None:
        return closest

    if abs(node.value - target) < abs(closest - target):
        closest = node.value

    closest = findClosestValueInBstLinearRecursive(node.left, target, closest)
    closest = findClosestValueInBstLinearRecursive(node.right, target, closest)
    return closest


"""
O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def findClosestValueInBstLinearIterative(root, target):
    stack = [root]
    closest = root.value

    while len(stack) > 0:
        node = stack.pop()

        if abs(node.value - target) < abs(closest - target):
            closest = node.value

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    return closest


"""
average: O(log(n)) time and O(1) space - if the input tree is balanced
worst: O(n) time and O(1) space
n is the number of nodes in the input tree
"""
def findClosestValueInBstLogarithmicIterative(node, target):
    currentNode = node
    closest = node.value

    while currentNode is not None:
        if abs(currentNode.value - target) < abs(closest - target):
            closest = currentNode.value

        if currentNode.value == target:
            break
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return closest