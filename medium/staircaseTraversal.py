from collections import deque

def staircaseTraversal(height, maxSteps):
    return staircaseTraversalRecursive(height, maxSteps, {0: 1, 1: 1})

"""
O(k*n) time and O(n) space
n is the height of the staircase
k is the number of allowed steps from 1 to maxSteps
"""
def staircaseTraversalRecursive(height, maxSteps, memo):
    if height in memo:
        return memo[height]

    result = 0
    for step in range(1, maxSteps + 1):
        if step <= height:
            result += staircaseTraversalRecursive(height - step, maxSteps, memo)

    memo[height] = result
    return result


"""
O(k*n) time and O(n) space
n is the height of the staircase
k is the number of allowed steps
"""
def staircaseTraversalIterative(height, maxSteps):
    dp = [0 for _ in range(0, height + 1)]
    dp[0] = 1
    dp[1] = 1

    for currentHeight in range(2, height + 1):
        step = 1
        while step <= min(currentHeight, maxSteps):
            dp[currentHeight] += dp[currentHeight - step]
            step += 1

    return dp[height]


"""
O(n) time and O(n) space
n is the height of the staircase
"""
def staircaseTraversalIterative(height, maxSteps):
    window = deque([1])
    windowSum = 0
    for currentHeight in range(1, height + 1):
        windowSum += window[-1]

        if currentHeight > maxSteps:
            windowSum -= window[0]
            window.popleft()

        window.append(windowSum)

    return windowSum