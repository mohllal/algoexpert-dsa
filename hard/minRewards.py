def minRewards(scores):
    return minRewardsQuadraticTimeAndLinearSpace(scores)


"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def minRewardsQuadraticTimeAndLinearSpace(scores):
    rewards = [1] * len(scores)

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
        else:
            for j in reversed(range(i)):
                if scores[j] > scores[j + 1]:
                    rewards[j] = max(rewards[j], rewards[j + 1] + 1)

    return sum(rewards)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def minRewardsLinearTimeAndLinearSpace(scores):
    rewards = [1] * len(scores)

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)