class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
O(n) time and O(1) space
n is the length of the input linked list
"""
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextUniqueNode = currentNode.next
        while nextUniqueNode is not None and nextUniqueNode.value == currentNode.value:
            nextUniqueNode = nextUniqueNode.next

        currentNode.next = nextUniqueNode
        currentNode = nextUniqueNode

    return linkedList