"""
O(n) time and O(n) space
n is the length of the input number string
"""
def bestDigits(number, numDigits):
    stack = []

    for i in range(0, len(number)):
        while len(stack) > 0 and int(stack[-1]) < int(number[i]) and numDigits > 0:
            stack.pop()
            numDigits -= 1

        stack.append(number[i])

    while numDigits > 0:
        stack.pop()
        numDigits -= 1

    return "".join(stack)