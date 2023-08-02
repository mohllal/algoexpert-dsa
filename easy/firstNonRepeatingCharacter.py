"""
O(n) time and O(1) space
n is the length of the input string
O(1) space because the input string has only lowercase english letters
"""
def firstNonRepeatingCharacter(string):
    counter = {}
    for character in string:
        if character not in counter:
            counter[character] = 0
        counter[character] += 1

    for index, character in enumerate(string):
        if counter[character] == 1:
            return index

    return -1