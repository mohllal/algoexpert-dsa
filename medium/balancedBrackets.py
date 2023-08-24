"""
O(n) time and O(n) space
n is the length of the input string
"""
def balancedBrackets(string):
    pairs = {"(": ")", "[": "]", "{": "}"}
    openingBrackets = "([{"
    closingBrackets = "}])"

    stack = []
    for character in string:
        if character not in openingBrackets and character not in closingBrackets:
            continue

        if character in openingBrackets:
            stack.append(character)
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()
            if pairs[top] != character:
                return False

    return len(stack) == 0
