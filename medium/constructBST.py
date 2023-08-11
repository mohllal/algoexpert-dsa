class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        insertRecursiveHelper(self, value)
        return self

    def contains(self, value):
        return containsRecursiveHelper(self, value)

    def remove(self, value):
        removeRecursiveHelper(self, value)
        return self


"""
average: O(log(n)) time and O(log(n)) space
worst: O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def containsRecursiveHelper(node, value):
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return containsRecursiveHelper(node.left, value)
    else:
        return containsRecursiveHelper(node.right, value)


"""
average: O(log(n)) time and O(1) space
worst: O(n) time and O(1) space
n is the number of nodes in the input tree
"""
def containsIterativeHelper(node, value):
    current = node
    while current is not None:
        if current.value == value:
            return True
        elif current.value > value:
            current = current.left
        else:
            current = current.right
    return False


"""
average: O(log(n)) time and O(log(n)) space
worst: O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def insertRecursiveHelper(node, value):
    if node is None:
        return BST(value)

    if node.value > value:
        node.left = insertRecursiveHelper(node.left, value)
    elif node.value <= value:
        node.right = insertRecursiveHelper(node.right, value)

    return node


"""
average: O(log(n)) time and O(1) space
worst: O(n) time and O(1) space
n is the number of nodes in the input tree
"""
def insertIterativeHelper(node, value):
    current = node
    while True:
        if current.value > value:
            if current.left is None:
                current.left = BST(value)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = BST(value)
                break
            else:
                current = current.right
    return node


def inOrderSuccessor(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


"""
average: O(log(n)) time and O(log(n)) space
worst: O(n) time and O(n) space
n is the number of nodes in the input tree
"""
def removeRecursiveHelper(node, value):
    if node is None:
        return node

    if node.value > value:
        node.left = removeRecursiveHelper(node.left, value)
    elif node.value < value:
        node.right = removeRecursiveHelper(node.right, value)
    else:
        # case 1: leaf node
        if node.left is None and node.right is None:
            return None
        # case 2.1: node with only right child
        elif node.left is None:
            node.value = node.right.value
            node.left = node.right.left
            node.right = node.right.right
            return node
        # case 2.2: node with only left child
        elif node.right is None:
            node.value = node.left.value
            node.right = node.left.right
            node.left = node.left.left
            return node
        # case 3: node with two children
        else:
            successor = inOrderSuccessor(node.right)
            node.value = successor.value
            node.right = removeRecursiveHelper(node.right, successor.value)
    return node


"""
average: O(log(n)) time and O(1) space
worst: O(n) time and O(1) space
n is the number of nodes in the input tree
"""
def removesIterativeHelper(node, value):
    current = node
    parent = None

    while current is not None and current.value != value:
        parent = current
        if current.value > value:
            current = current.left
        else:
            current = current.right

    if current is None:
        return node

    # case 1: leaf node
    if current.left is None and current.right is None:
        # if the node to be deleted is not a root node
        if current != node:
          if parent.left == current:
              parent.left = None
          else:
              parent.right = None
    # case 2.1: node with only right child
    elif current.left is None:
        current.value = current.right.value
        current.left = current.right.left
        current.right = current.right.right
    # case 2.1: node with only left child
    elif current.right is None:
        current.value = current.left.value
        current.right = current.left.right
        current.left = current.left.left
    # case 3: node with two children
    else:
      successor = inOrderSuccessor(current.right)
      current.value = successor.value
      current.right = removesIterativeHelper(current.right, successor.value)

    return node



