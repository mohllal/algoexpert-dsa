def isPalindrome(string):
    return isPalindromeLinearTimeAndLinearSpace(string)


"""
O(n) time and O(n) space
n is the length of the input string
"""
def isPalindromeLinearTimeAndLinearSpace(string):
    return string == ''.join(reversed(string))


"""
O(n) time and O(1) space
n is the length of the input string
"""
def isPalindromeLinearTimeAndConstantSpace(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True


"""
O(n) time and O(1) space
n is the length of the input string
O(n) space if not a tail recursion case
"""
def isPalindromeRecursiveLinearTimeAndConstantSpace(string, start=0):
    end = len(string) - start - 1
    if start >= end:
        return True
    if string[start] != string[end]:
        return False
    return isPalindromeRecursiveLinearTimeAndConstantSpace(string, start + 1)