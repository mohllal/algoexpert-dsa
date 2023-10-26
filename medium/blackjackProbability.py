"""
O(n) time and O(n) space
n is the difference between the target and the starting hand
"""
def blackjackProbability(target, startingHand):
    def blackjackProbabilityHelper(target, startingHand, memo):
        if startingHand > target:
            return 1.0

        if startingHand >= target - 4:
            return 0.0

        if startingHand in memo:
            return memo[startingHand]

        bust = 0.0
        for draw in range(1, 11):
            bust += 0.1 * blackjackProbabilityHelper(target, startingHand + draw, memo)

        memo[startingHand] = round(bust, 3)
        return memo[startingHand]

    return blackjackProbabilityHelper(target, startingHand, {})