def longestPeak(array):
    return longestPeakLinearTimeAndConstantSpace(array)


"""
O(n^2) time and O(1) space
n is the length of the input array
"""
def longestPeakQuadraticTimeAndConstantSpace(array):
    longest = 0
    for i in range(0, len(array)):
        j = i

        increasing = False
        while j < len(array) - 1 and array[j] < array[j + 1]:
            j += 1
            increasing = True

        decreasing = False
        while j < len(array) - 1 and array[j] > array[j + 1]:
            j += 1
            decreasing = True

        if increasing and decreasing:
            longest = max(longest, j - i + 1)

    return longest


"""
O(n) time and O(1) space
n is the length of the input array
"""
def longestPeakLinearTimeAndConstantSpace(array):
    longest = 0

    i = 0
    while i < len(array):
        j = i

        increasing = False
        while j < len(array) - 1 and array[j] < array[j + 1]:
            j += 1
            increasing = True

        decreasing = False
        while j < len(array) - 1 and array[j] > array[j + 1] and increasing:
            j += 1
            decreasing = True

        if increasing and decreasing:
            longest = max(longest, j - i + 1)
            i = j
        else:
            i = j + 1

    return longest


"""
O(n) time and O(1) space
n is the length of the input array
"""
def longestPeakAnotherLinearTimeAndConstantSpace(array):
    longest = 0

    i = 1
    while i < len(array) - 1:
        isPeak =  array[i] > array[i - 1] and array[i] > array[i + 1]

        if not isPeak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        longest = max(longest, right - left - 1)
        i = right
    return longest