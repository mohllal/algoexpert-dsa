def missingNumbers(nums):
    return missingNumbersLinearTimeAndConstantSpace(nums)


"""
O(nlog(n)) time and O(1) space
n is the length of the input array
"""
def missingNumbersLogLinearTimeAndConstantSpace(nums):
    nums.sort()

    missing = []
    pointer, current = 0, 1
    while current <= len(nums) + 2:
        if pointer >= len(nums) or nums[pointer] != current:
            missing.append(current)
            current += 1
        else:
            current += 1
            pointer += 1

    return missing


"""
O(n) time and O(n) space
n is the length of the input array
"""
def missingNumbersLinearTimeAndLinearSpace(nums):
    exists = set(nums)

    missing = []
    for i in range(1, len(nums) + 3):
        if i not in exists:
            missing.append(i)
    return missing


"""
O(n) time and O(1) space
n is the length of the input array
"""
def missingNumbersLinearTimeAndConstantSpace(nums):
    nPlusTwo = len(nums) + 2
    nPlusTwoSum = (nPlusTwo * (nPlusTwo + 1)) // 2

    numsSum = sum(nums)
    missingTotal = nPlusTwoSum - numsSum
    missingAverage = missingTotal // 2

    numsAverageLeftHalf = 0
    numsAverageRightHalf = 0
    for i in range(0, len(nums)):
        if nums[i] <= missingAverage:
            numsAverageLeftHalf += nums[i]
        else:
            numsAverageRightHalf += nums[i]

    leftAverageTotalSum = (missingAverage * (missingAverage + 1)) // 2

    leftMissingNum = leftAverageTotalSum - numsAverageLeftHalf
    rightMissingNum = nPlusTwoSum - (leftMissingNum + numsSum)

    return [leftMissingNum, rightMissingNum]