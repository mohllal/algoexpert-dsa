"""
O(n) time and O(n) space
n is the length of the input array
"""
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for i in range(0, 2 * len(array)):
        index = i % len(array)

        while len(stack) > 0 and array[stack[-1]] < array[index]:
            top = stack.pop()
            result[top] = array[index]

        stack.append(index)

    return result