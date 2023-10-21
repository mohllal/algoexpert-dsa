def minNumberOfCoinsForChange(n, denoms):
    return minNumberOfCoinsForChangeRecursive(n, denoms)


"""
O(n*m) time and O(n*m) space
n is the target amount
m is the length of the coins input array
"""
def minNumberOfCoinsForChangeRecursive(n, denoms):
    def minNumberOfCoinsForChangeHelper(n, denoms, memo):
        if n == 0:
            return 0

        if n in memo:
            return memo[n]

        numOfCoins = float("inf")
        for coin in denoms:
            if n >= coin:
                currNumOfCoins = minNumberOfCoinsForChangeHelper(n - coin, denoms, memo) + 1
                numOfCoins = min(numOfCoins, currNumOfCoins)

        memo[n] = numOfCoins
        return numOfCoins

    numOfCoins = minNumberOfCoinsForChangeHelper(n, denoms, {})
    return numOfCoins if numOfCoins != float("inf") else -1


"""
O(n*m) time and O(n) space
n is the target amount
m is the length of the coins input array
"""
def minNumberOfCoinsForChangeIterative(n, denoms):
    numOfCoins = [float("inf") for _ in range(n + 1)]
    numOfCoins[0] = 0

    for coin in denoms:
        for target in range(1, n + 1):
            if target >= coin:
                currNumOfCoins = numOfCoins[target - coin] + 1
                numOfCoins[target] = min(numOfCoins[target], currNumOfCoins)

    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1