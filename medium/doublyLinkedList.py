class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    """
    O(1) time and O(1) space
    """
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)


    """
    O(1) time and O(1) space
    """
    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.insertAfter(self.tail, node)


    """
    O(1) time and O(1) space
    """
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node == self.head:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert


    """
    O(1) time and O(1) space
    """
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node == self.tail:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert


    """
    O(p) time and O(1) space
    p is the position to insert at
    """
    def insertAtPosition(self, position, nodeToInsert):
        current = self.head
        currentPosition = 1

        while current is not None and currentPosition != position:
            current = current.next
            currentPosition += 1

        if currentPosition == position:
            current.prev.next = nodeToInsert
            nodeToInsert.prev = current.prev
            nodeToInsert.next = current


    """
    O(n) time and O(1) space
    n is the number of nodes in the input list
    """
    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            temp = current
            current = current.next
            if temp.value == value:
                self.remove(temp)


    """
    O(1) time and O(1) space
    """
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None


    """
    O(n) time and O(1) space
    n is the number of nodes in the input list
    """
    def containsNodeWithValue(self, value):
        current = self.head
        while current is not None and current.value != value:
            current = current.next

        return current is not None