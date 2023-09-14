class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    return removeKthNodeFromEndLinearTimeAndConstantTime(head, k)


"""
O(n) time and O(1) space
n is the number of nodes in the input list
"""
def removeKthNodeFromEndLinearTimeAndConstantTime(head, k):
    length = 1
    node = head
    while node.next is not None:
        node = node.next
        length += 1

    target = length - k

    current = 0
    node = head
    while node is not None:
        if current >= target:
            temp = node.next.value
            node.next.value = node.value
            node.value = temp

        if current == length - 2:
            node.next = None

        node = node.next
        current += 1

    return head


"""
O(n) time and O(n) space
n is the number of nodes in the input list
"""
def removeKthNodeFromRecursiveLinearTimeAndLinearSpace(head, k):
    current = removeKthNodeFromRecursive(head, k)

    if current == k:
        head.value = head.next.value
        head.next = head.next.next

    return head


def removeKthNodeFromRecursive(node, k):
    if node is None:
        return 0

    current = removeKthNodeFromRecursive(node.next, k)

    if current == k:
        node.next = node.next.next

    return current + 1