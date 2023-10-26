def levenshteinDistance(str1, str2):
    return levenshteinDistanceRecursive(str1, str2)


"""
O(n*m) time and O(n*m) space
n is the length of the first input string
m is the length of the second input string
"""
def levenshteinDistanceRecursive(str1, str2):
    def levenshteinDistanceHelper(str1, idx1, str2, idx2, memo):
        if idx1 == len(str1):
            return len(str2) - idx2

        if idx2 == len(str2):
            return len(str1) - idx1

        if memo[idx1][idx2] != -1:
            return memo[idx1][idx2]

        delta = 1 if str1[idx1] != str2[idx2] else 0
        memo[idx1][idx2] = min(
            levenshteinDistanceHelper(str1, idx1 + 1, str2, idx2 + 1, memo) + delta,
            levenshteinDistanceHelper(str1, idx1 + 1, str2, idx2, memo) + 1,
            levenshteinDistanceHelper(str1, idx1, str2, idx2 + 1, memo) + 1
        )

        return memo[idx1][idx2]

    memo = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]
    return levenshteinDistanceHelper(str1, 0, str2, 0, memo)

"""
O(n*m) time and O(n*m) space
n is the length of the first input string
m is the length of the second input string
"""
def levenshteinDistanceIterative(str1, str2):
    edits = [[float("inf") for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    for i in range(len(str1) + 1):
        edits[0][i] = i

    for j in range(len(str2) + 1):
        edits[j][0] = j

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])

    return edits[-1][-1]


"""
O(n*m) time and O(min(n,m)) space
n is the length of the first input string
m is the length of the second input string
"""
def levenshteinDistanceMemoryOptimizedIterative(str1, str2):
    longStr = str1 if len(str1) >= len(str2) else str2
    shortStr = str1 if len(str1) < len(str2) else str2

    previous = [i for i in range(len(shortStr) + 1)]
    current = [float("inf") for _ in range(len(shortStr) + 1)]

    for i in range(1, len(longStr) + 1):
        current[0] = i

        for j in range(1, len(shortStr) + 1):
            if longStr[i - 1] == shortStr[j - 1]:
                current[j] = previous[j - 1]
            else:
                current[j] = 1 + min(previous[j], previous[j - 1], current[j - 1])

        previous, current = current, previous
    return previous[-1]