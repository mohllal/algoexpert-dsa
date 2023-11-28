class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
O(n) time and O(h) space
n is the number of nodes in the input BST
h is the maximum depth of the input BST
"""
def repairBst(tree):
    firstNode = secondNode = previousNode = None

    def repairBstHelper(node):
        nonlocal firstNode, secondNode, previousNode

        if node is None:
            return

        repairBstHelper(node.left)

        if previousNode is not None and previousNode.value > node.value:
            if firstNode is None:
                firstNode = previousNode

            secondNode = node

        previousNode = node
        repairBstHelper(node.right)

    repairBstHelper(tree)
    firstNode.value, secondNode.value = secondNode.value, firstNode.value
    return tree
