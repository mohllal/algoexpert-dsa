"""
O(nlog(n)) time and O(1) space
n is the length of the input array
"""
def nonConstructibleChange(coins):
    coins.sort()

    minimum = 0
    for i in range(0, len(coins)):
        if coins[i] > minimum + 1:
            return minimum + 1

        minimum += coins[i]

    return minimum + 1
