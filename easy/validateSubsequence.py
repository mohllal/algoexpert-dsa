def isValidSubsequence(array, sequence):
    return isValidSubsequenceQuadraticTimeAndConstantSpace(array, sequence)


"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def isValidSubsequenceQuadraticTimeAndConstantSpace(array, sequence):
    if len(sequence) > len(array):
        return False

    start = 0
    for i in range(0, len(sequence)):
        exists = False

        for j in range(start, len(array)):
            if array[j] == sequence[i]:
                start = j + 1
                exists = True
                break
        if not exists:
            return False

    return True


"""
O(n) time and O(1) space
n is the length of the input array
"""
def isValidSubsequenceLinearTimeAndConstantSpace(array, sequence):
    if len(sequence) > len(array):
        return False

    j = 0
    for i in range(0, len(array)):
        if j == len(sequence):
            break
        if array[i] == sequence[j]:
            j += 1

    return j == len(sequence)
