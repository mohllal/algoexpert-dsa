def longestSubarrayWithSum(array, targetSum):
    return longestSubarrayWithSumQuadraticTimeAndConstantSpace(array, targetSum)


"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def longestSubarrayWithSumQuadraticTimeAndConstantSpace(array, targetSum):
    maxWindowLength = float("-inf")
    result = []

    for currWindowStart in range(len(array)):
        currWindowSum = 0

        for currWindowEnd in range(currWindowStart, len(array)):
            currWindowSum += array[currWindowEnd]
            currWindowLength = currWindowEnd - currWindowStart

            if currWindowSum == targetSum and currWindowLength > maxWindowLength:
                maxWindowLength = currWindowEnd - currWindowStart
                result = [currWindowStart, currWindowEnd]

    return result


"""
O(n) time and O(1) space
n is the length of the input array
"""
def longestSubarrayWithSumLinearTimeAndConstantSpace(array, targetSum):
    currWindowSum = 0
    currWindowStart = 0

    maxWindowLength = float("-inf")
    result = []
    for currWindowEnd in range(len(array)):
        currWindowSum += array[currWindowEnd]

        while currWindowStart < currWindowEnd and currWindowSum > targetSum:
            currWindowSum -= array[currWindowStart]
            currWindowStart += 1

        currWindowLength = currWindowEnd - currWindowStart
        if currWindowSum == targetSum and currWindowLength > maxWindowLength:
            maxWindowLength = currWindowLength
            result = [currWindowStart, currWindowEnd]

    return result