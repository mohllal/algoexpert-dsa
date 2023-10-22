def numberOfWaysToTraverseGraph(width, height):
    return numberOfWaysToTraverseGraphRecursive(width, height)

"""
O(2^(w+h)) time and O(w+h) space
w is the input width
h is the input height
"""
def numberOfWaysToTraverseGraphRecursive(width, height):
    if width == 1 or height == 1:
        return 1

    return (
        numberOfWaysToTraverseGraphRecursive(width - 1, height) +
        numberOfWaysToTraverseGraphRecursive(width, height - 1)
    )


"""
O(w*h) time and O(w*h) space
w is the input width
h is the input height
"""
def numberOfWaysToTraverseGraphMemoizedRecursive(width, height):
    def numberOfWaysToTraverseGraphHelper(width, height, memo):
        if width == 1 or height == 1:
            return 1

        if memo[height][width] != -1:
            return memo[height][width]

        memo[height][width] = (
            numberOfWaysToTraverseGraphHelper(width - 1, height, memo) +
            numberOfWaysToTraverseGraphHelper(width, height - 1, memo)
        )

        return memo[height][width]

    memo = [[-1 for _ in range(width + 1)] for _ in range(height + 1)]
    return numberOfWaysToTraverseGraphHelper(width, height, memo)


"""
O(w+h) time and O(1) space
w is the input width
h is the input height
"""
def numberOfWaysToTraverseGraphIterative(width, height):
    xDistanceToCorner = width - 1
    yDistanceToCorner = height - 1

    # C(n, r) = n! / r! * (n-r)!
    # C(x + y, x) = (x + y)! / x! * y!

    numerator = factorial(xDistanceToCorner + yDistanceToCorner)
    denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)

    return numerator // denominator