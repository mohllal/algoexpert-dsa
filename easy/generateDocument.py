def generateDocument(characters, document):
    return generateDocumentLinearTimeAndLinearSpace(characters, document)


"""
O(n+m) time and O(c) space
n is the length of the characters string
m is the length of the document string
c is the number of unique characters in the characters string
"""
def generateDocumentLinearTimeAndLinearSpace(characters, document):
    occurrences = {}
    for character in characters:
        occurrences[character] = (
            1 if character not in occurrences
            else occurrences[character] + 1
        )

    for character in document:
        if character not in occurrences or occurrences[character] < 1:
            return False
        occurrences[character] -= 1

    return True


"""
O(n+m) time and O(c+d) space
n is the length of the characters string
m is the length of the document string
c is the number of unique characters in the characters string
d is the number of unique characters in the document string
"""
def generateDocumentAnotherLinearTimeAndLinearSpace(characters, document):
    occurrences = {}
    for character in characters:
        occurrences[character] = (
            1 if character not in occurrences
            else occurrences[character] + 1
        )

    for character in document:
        if character not in occurrences or occurrences[character] < 1:
            return False
        occurrences[character] -= 1

    return True