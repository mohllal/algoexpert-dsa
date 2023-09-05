class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k, array=None):
    values = findKthLargestValueInBstLinearTimeAndLinearSpace(tree)
    return values[-k]


"""
O(n) time and O(n) space
n is the number of nodes of the input BST
"""
def findKthLargestValueInBstLinearTimeAndLinearSpace(tree, values=None):
    if values is None:
        values = []

    if tree is None:
        return

    findKthLargestValueInBstLinearTimeAndLinearSpace(tree.left, values)
    values.append(tree.value)
    findKthLargestValueInBstLinearTimeAndLinearSpace(tree.right, values)
    return values

"""
O(d+k) time and O(d) space
d is the height of the input BST
"""
def findKthLargestValueInBstAnotherLinearTimeAndLinearSpace(tree, k):
    result = None

    def findKthLargestValueInBstHelper(tree):
        nonlocal result
        nonlocal k

        if tree is None:
            return

        findKthLargestValueInBstHelper(tree.right)

        if k == 0:
            return

        result = tree.value
        k -= 1

        findKthLargestValueInBstHelper(tree.left)

    findKthLargestValueInBstHelper(tree)
    return result