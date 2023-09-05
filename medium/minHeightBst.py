class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightBst(array):
    root = minHeightBstLogLinearTimeAndLinearSpace(array, 0, len(array) - 1)
    return root


"""
O(nlog(n)) time and O(n) space
n is the length of the input array
"""
def minHeightBstLogLinearTimeAndLinearSpace(array, start, end, node=None):
    if start > end:
        return

    mid = (start + end) // 2
    if node is None:
        node = BST(array[mid])
    else:
        node.insert(array[mid])

    minHeightBstLogLinearTimeAndLinearSpace(array, start, mid - 1, node)
    minHeightBstLogLinearTimeAndLinearSpace(array, mid + 1, end, node)
    return node


"""
O(n) time and O(n) space
n is the length of the input array
"""
def minHeightBstLinearTimeAndLinearSpace(array, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    node = BST(array[mid])

    node.left = minHeightBstLinearTimeAndLinearSpace(array, start, mid - 1)
    node.right = minHeightBstLinearTimeAndLinearSpace(array, mid + 1, end)
    return node