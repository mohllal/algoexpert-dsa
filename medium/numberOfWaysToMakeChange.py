def numberOfWaysToMakeChange(n, denoms):
    return numberOfWaysToMakeChangeMemoizedRecursive(n, denoms)


"""
O(2^m) time and O(m) space
m is the length of the coins input array
"""
def numberOfWaysToMakeChangeRecursive(n, denoms):
    def numberOfWaysToMakeChangeHelper(n, index, denoms):
        if n == 0:
            return 1

        if n < 0:
            return 0

        if index == len(denoms):
            return 0

        return (
            numberOfWaysToMakeChangeHelper(n - denoms[index], index, denoms) +
            numberOfWaysToMakeChangeHelper(n, index + 1, denoms)
        )

    return numberOfWaysToMakeChangeHelper(n, 0, denoms)


"""
O(n*m) time and O(n*m) space
n is the n amount
m is the length of the coins input array
"""
def numberOfWaysToMakeChangeMemoizedRecursive(n, denoms):
    def numberOfWaysToMakeChangeHelper(n, index, denoms, memo):
        if n == 0:
            return 1

        if n < 0:
            return 0

        if index == len(denoms):
            return 0

        if memo[index][n] != -1:
            return memo[index][n]

        memo[index][n] = (
            numberOfWaysToMakeChangeHelper(n - denoms[index], index, denoms, memo) +
            numberOfWaysToMakeChangeHelper(n, index + 1, denoms, memo)
        )

        return memo[index][n]

    memo = [[-1 for _ in range(n + 1)] for _ in range(len(denoms))]
    return numberOfWaysToMakeChangeHelper(n, 0, denoms, memo)


"""
O(n*m) time and O(n) space
n is the n amount
m is the length of the coins input array
"""
def numberOfWaysToMakeChangeIterative(n, denoms):
    numOfWays = [0 for _ in range(n + 1)]
    numOfWays[0] = 1

    for coin in denoms:
        for n in range(1, n + 1):
            if n >= coin:
                numOfWays[n] += numOfWays[n - coin]

    return numOfWays[n]