"""
O(n) time and O(n) space
n is the length of the input array
"""
def reversePolishNotation(tokens):
    operator = set(["+", "-", "*", "/"])
    stack = []

    for token in tokens:
        if token not in operator:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                result = int(left / right)

            stack.append(result)

    return stack[0]