class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
O(n + m) time and O(n + m) space
n is the number of nodes in the first input list
m is the number of nodes in the second input list
"""
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    firstListValue = getListValue(linkedListOne)
    secondListValue = getListValue(linkedListTwo)
    outputListValue = str(firstListValue + secondListValue)

    head = None
    prev = None
    for i in range(len(outputListValue) - 1, -1, -1):
        node = LinkedList(int(outputListValue[i]))
        if prev is None:
            head = node
        else:
            prev.next = node
        prev = node

    return head


def getListValue(linkedList):
    node = linkedList
    result = 0
    powerOfTen = 0
    while node is not None:
        result += node.value * (10 ** powerOfTen)

        powerOfTen += 1
        node = node.next

    return result