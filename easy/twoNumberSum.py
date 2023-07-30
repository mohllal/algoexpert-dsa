def twoNumberSum(array, targetSum):
    return twoNumberSumQuadraticTimeAndConstantSpace(array, targetSum)


"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def twoNumberSumQuadraticTimeAndConstantSpace(array, targetSum):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


"""
O(n) time and O(n) space
n is the length of the input array
"""
def twoNumberSumLinearTimeAndLinearSpace(array, targetSum):
    hashmap = {}

    for num in array:
        diff = targetSum - num
        if diff in hashmap:
            return [diff, num]
        hashmap[num] = True

    return []


"""
O(nlog(n)) time and O(1) space
n is the length of the input array
"""
def twoNumberSumLogLinearTimeAndConstantSpace(array, targetSum):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == targetSum:
            return [array[right], array[left]]

        if currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []
