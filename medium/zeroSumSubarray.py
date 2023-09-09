"""
O(n) time and O(n) space
n is the length of the input array
"""
def zeroSumSubarray(nums):
    current = 0
    prefix = [0] * len(nums)
    for i in range(0, len(nums)):
        prefix[i] = nums[i] + current
        current += nums[i]

    unique = set()
    for i in range(0, len(prefix)):
        if prefix[i] == 0 or prefix[i] in unique:
            return True
        unique.add(prefix[i])

    return False