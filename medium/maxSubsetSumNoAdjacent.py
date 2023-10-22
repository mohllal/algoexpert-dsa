def maxSubsetSumNoAdjacent(array):
    return maxSubsetSumNoAdjacentMemoizedRecursive(array)

"""
O(2^n) time and O(n) space
n is the length of the input array
"""
def maxSubsetSumNoAdjacentRecursive(array):
    def maxSubsetSumNoAdjacentHelper(array, index):
        if index >= len(array):
            return 0

        return max(
            array[index] + maxSubsetSumNoAdjacentHelper(array, index + 2),
            maxSubsetSumNoAdjacentHelper(array, index + 1)
        )

    return maxSubsetSumNoAdjacentHelper(array, 0)

"""
O(n) time and O(n) space
n is the length of the input array
"""
def maxSubsetSumNoAdjacentMemoizedRecursive(array):
    def maxSubsetSumNoAdjacentHelper(array, index, memo):
        if index >= len(array):
            return 0

        if memo[index] != -1:
            return memo[index]

        memo[index] = max(
            array[index] + maxSubsetSumNoAdjacentHelper(array, index + 2, memo),
            maxSubsetSumNoAdjacentHelper(array, index + 1, memo)
        )

        return memo[index]

    memo = [-1 for _ in range(len(array))]
    return maxSubsetSumNoAdjacentHelper(array, 0, memo)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def maxSubsetSumNoAdjacentIterative(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    maxSubsetSum = [0 for _ in range(len(array))]
    maxSubsetSum[0] = array[0]
    maxSubsetSum[1] = max(array[1], array[0])

    for i in range(2, len(array)):
        maxSubsetSum[i] = max(
            maxSubsetSum[i - 2] + array[i],
            maxSubsetSum[i - 1]
        )

    return maxSubsetSum[-1]

"""
O(n) time and O(1) space
n is the length of the input array
"""
def maxSubsetSumNoAdjacentMemoryOptimizedIterative(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    latterMax = array[0]
    lastMax = max(array[1], array[0])

    for i in range(2, len(array)):
        current = max(latterMax + array[i], lastMax)

        latterMax = lastMax
        lastMax = current

    return lastMax