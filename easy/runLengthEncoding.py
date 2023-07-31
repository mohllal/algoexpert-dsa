"""
O(n) time and O(n) space
n is the length of the input string
"""
def runLengthEncoding(string):
    encoded = []

    currentRunLength = 1
    for i in range(1, len(string)):
        if string[i] != string[i-1] or currentRunLength == 9:
            encoded.append(str(currentRunLength))
            encoded.append(string[i-1])
            currentRunLength = 0

        currentRunLength += 1

    encoded.append(str(currentRunLength))
    encoded.append(string[-1])

    return "".join(encoded)