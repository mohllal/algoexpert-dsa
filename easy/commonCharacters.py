def commonCharacters(strings):
    return commonCharactersLinearQuadraticTimeAndLinearSpace(strings)


"""
O(n*m) time and O(m) space
n is the length of the input array
m is the length of the longest string
"""
def commonCharactersLinearQuadraticTimeAndLinearSpace(strings):
    smallestString = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) < len(smallestString):
            smallestString = strings[i]

    commonCharacters = set(smallestString)
    for string in strings:
        stringCharacters = set(string)
        for character in list(commonCharacters):
            if character not in stringCharacters:
                commonCharacters.remove(character)

    return list(commonCharacters)


"""
O(n*m) time and O(c) space
n is the length of the input array
m is the length of the longest string
c is the number of unique characters across all strings
"""
def commonCharactersAnotherLinearQuadraticTimeAndLinearSpace(strings):
    counter = {}
    for string in strings:
        uniqueCharacters = set(string)
        for character in uniqueCharacters:
            if character not in counter:
                counter[character] = 0
            counter[character] += 1

    result = []
    for character in counter:
        if counter[character] == len(strings):
            result.append(character)

    return result