from collections import Counter


"""
O(n*w) time and O(h) space
n is the length of the input array
w is the length of the longest word
h is the number of unique characters in all words
"""
def minimumCharactersForWords(words):
    result = []
    aCounter = {}

    for word in words:
        wCounter = Counter(word)

        for character in wCounter.keys():
            wCount = wCounter[character]
            aCount = aCounter[character] if character in aCounter else 0
            aCounter[character] = max(wCount, aCount)

    for character, count in aCounter.items():
        result.extend([character] * count)

    return result