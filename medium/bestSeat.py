"""
O(n) time and O(1) space
n is the length of the input array
"""
def bestSeat(seats):
    slow = 0

    longest = float("-inf")
    result = -1
    while slow < len(seats):
        if seats[slow] == 1:
            slow += 1
            continue

        fast = slow + 1
        while fast < len(seats) and seats[fast] == 0:
            fast += 1

        length = fast - slow + 1
        if length > longest:
            longest = length
            result = slow + (length // 2) - 1

        slow = fast

    return result