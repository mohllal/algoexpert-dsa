class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
O(n + m) time and O(1) space
n is the number of nodes in first input list
m is the number of nodes in second input list
"""
def mergingLinkedLists(linkedListOne, linkedListTwo):
    linkedListOneLength = linkedListLength(linkedListOne)
    linkedListTwoLength = linkedListLength(linkedListTwo)

    largeLinkedList = None
    smallLinkedList = None
    startNodeIndex = None
    if linkedListOneLength >= linkedListTwoLength:
        largeLinkedList = linkedListOne
        smallLinkedList = linkedListTwo
        startNodeIndex = linkedListOneLength - linkedListTwoLength
    else:
        largeLinkedList = linkedListTwo
        smallLinkedList = linkedListOne
        startNodeIndex = linkedListTwoLength - linkedListOneLength

    currentNodeIndex = 0
    while largeLinkedList is not None and currentNodeIndex < startNodeIndex:
        largeLinkedList = largeLinkedList.next
        currentNodeIndex += 1

    intersect = False
    result = None
    while largeLinkedList is not None and smallLinkedList is not None:
        if intersect == False and largeLinkedList.value == smallLinkedList.value:
            result = largeLinkedList
            intersect = True

        if intersect == True and largeLinkedList.value != smallLinkedList.value:
            result = None
            break

        largeLinkedList = largeLinkedList.next
        smallLinkedList = smallLinkedList.next

    return result


def linkedListLength(linkedList):
    length = 0

    node = linkedList
    while node is not None:
        length += 1
        node = node.next

    return length