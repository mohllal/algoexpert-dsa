def reverseWordsInString(string):
    return reverseWordsInStringRecursiveLinearTimeAndLinearSpace(string)

"""
O(n) time and O(n) space
n is the length of the input string
"""
def reverseWordsInStringLinearTimeAndLinearSpace(string):
    reverse = []
    word = []
    for i in range(len(string) - 1, -1, -1):
        if string[i] != ' ':
            word.append(string[i])
            continue

        while len(word) > 0:
            reverse.append(word.pop())

        reverse.append(string[i])

    while len(word) > 0:
        reverse.append(word.pop())
    return "".join(reverse)


"""
O(n) time and O(n) space
n is the length of the input string
"""
def reverseWordsInStringAnotherLinearTimeAndLinearSpace(string):
    reverse = []
    startOfWord = len(string) - 1
    endOfWord = len(string) - 1
    for i in range(len(string) - 1, -1, -1):
        if string[i] == ' ':
            reverse.append(string[startOfWord+1:endOfWord+1])
            reverse.append(string[i])
            startOfWord = i - 1
            endOfWord = i - 1
        else:
           startOfWord -= 1

    reverse.append(string[startOfWord+1:endOfWord+1])
    return "".join(reverse)


"""
O(n) time and O(n) space
n is the length of the input string
"""
def reverseWordsInStringRecursiveLinearTimeAndLinearSpace(string):
    if string == "":
        return string

    spaceIndex = string.find(" ")
    if spaceIndex == -1:
        return string

    beforeSpace = string[:spaceIndex]
    afterSpace = string[spaceIndex + 1:]

    afterReverse = reverseWordsInStringRecursiveLinearTimeAndLinearSpace(afterSpace)

    return afterReverse + " " + beforeSpace