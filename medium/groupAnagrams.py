def groupAnagrams(words):
    return groupAnagramsThird(words)


"""
O(n^2*w) time and O(n^2*w) space
n is the length of the input array
w is the length of the longest word
"""
def groupAnagramsFirst(words):
    visited = set()

    result = []
    for i in range(0, len(words)):
        if words[i] in visited:
            continue

        anagrams = []
        for j in range(i + 1, len(words)):
            if words[j] in visited:
                continue

            if areAnagrams(words[i], words[j]):
                anagrams.append(words[j])

        anagrams.append(words[i])
        visited.update(anagrams)
        result.append(anagrams)

    return result


def areAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    characters = {}

    for character in str1:
        if character not in characters:
            characters[character] = 0
        characters[character] += 1

    for character in str2:
        if character not in characters:
            return False
        characters[character] -= 1

    for character in characters:
        if characters[character] != 0:
            return False

    return True


"""
O(n*wlog(w) + w*nlog(n)) time and O(n*w) space
n is the length of the input array
w is the length of the longest word
"""
def groupAnagramsSecond(words):
    sWords = [(words[i], i) for i in range(0, len(words))]

    for i in range(0, len(sWords)):
        sortedWord = sorted(sWords[i][0])
        sWords[i] = (sortedWord, sWords[i][1])

    sWords.sort(key=lambda x: x[0])

    result = []
    anagrams = []
    for i in range(0, len(sWords)):
        if len(anagrams) == 0:
            anagrams.append(words[sWords[i][1]])
            continue

        if sWords[i][0] == sWords[i - 1][0]:
            anagrams.append(words[sWords[i][1]])
        else:
            result.append(anagrams)
            anagrams = [words[sWords[i][1]]]

    if len(anagrams) > 0:
        result.append(anagrams)

    return result


"""
O(n*wlog(w)) O(n*w) space
n is the length of the input array
w is the length of the longest word
"""
def groupAnagramsThird(words):
    anagrams = {}

    for word in words:
        sWord = str(sorted(word))

        if sWord not in anagrams:
            anagrams[sWord] = [word]
        else:
            anagrams[sWord].append(word)

    result = []
    for anagram in anagrams:
        result.append(anagrams[anagram])

    return result