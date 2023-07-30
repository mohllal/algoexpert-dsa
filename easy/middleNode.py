class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    return middleNodeLinearTimeAndLinearSpace(linkedList)


"""
O(n) time and O(n) space
n is the length of the input linked list
"""
def middleNodeLinearTimeAndLinearSpace(linkedList):
    nodes = []

    currentNode = linkedList
    while currentNode is not None:
        nodes.append(currentNode)
        currentNode = currentNode.next

    return nodes[len(nodes) // 2]


"""
O(n) time and O(1) space
n is the length of the input input linked list
"""
def middleNodeLinearTimeAndConstantSpace(linkedList):
    linkedListLength = 0
    currentNode = linkedList
    while currentNode is not None:
        linkedListLength += 1
        currentNode = currentNode.next

    currentNode = linkedList
    for _ in range(0, linkedListLength // 2):
        currentNode = currentNode.next

    return currentNode
