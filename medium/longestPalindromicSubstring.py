def longestPalindromicSubstring(string):
    return longestPalindromicSubstringQuadraticTimeAndLinearSpace(string)

"""
O(n^3) time and O(n) space
n is the length of the input string
"""
def longestPalindromicSubstringCubicTimeAndLinearSpace(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            current = string[i:j]
            if isPalindrome(current) and len(current) > len(longest):
                longest = current

    return longest


def isPalindrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


"""
O(n^2) time and O(n) space
n is the length of the input string
"""
def longestPalindromicSubstringQuadraticTimeAndLinearSpace(string):
    longest = ""

    for i in range(0, len(string)):
        longestEventLengthPalindrome = longestPalindromicSubstringAroundIndex(string, i, i + 1)
        longestOddLengthPalindrome = longestPalindromicSubstringAroundIndex(string, i - 1, i + 1)

        if len(longestEventLengthPalindrome) > len(longest):
            longest = longestEventLengthPalindrome

        if len(longestOddLengthPalindrome) > len(longest):
            longest = longestOddLengthPalindrome

    return longest


def longestPalindromicSubstringAroundIndex(string, left, right):
    while right < len(string) and left >= 0 and string[right] == string[left]:
        right += 1
        left -= 1

    return string[left+1:right]