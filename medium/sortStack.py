"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def sortStack(stack):
    if len(stack) == 0:
        return stack

    current = stack.pop()
    sortStack(stack)

    insertElement(stack, current)
    return stack


"""
O(n) time and O(n) space
n is the length of the input array
"""
def insertElement(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
        return

    current = stack.pop()
    insertElement(stack, element)

    stack.append(current)
    return stack