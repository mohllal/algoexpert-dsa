def semordnilap(words):
    return semordnilapLinearQuadraticTimeAndLinearQuadraticSpace(words)


"""
O(n*m) time and O(n*m) space
n is the length of the input array
m is the length of the longest word
"""
def semordnilapLinearQuadraticTimeAndLinearQuadraticSpace(words):
    pairs = []
    exists = set(words)

    for word in words:
        reverse = word[::-1]
        if word != reverse and reverse in exists:
            pairs.append([word, reverse])
            exists.discard(reverse)
            exists.discard(word)

    return pairs


"""
O((n^2)+(n*m)) time and O(n*m) space
n is the length of the input array
m is the length of the longest word
"""
def semordnilapAnotherLinearQuadraticTimeAndLinearQuadraticSpace(words):
    pairs = []

    for i in range(0, len(words)):
        reverse = words[i][::-1]
        for j in range(i + 1, len(words)):
            if words[j] == reverse:
                pairs.append([words[i], words[j]])

    return pairs