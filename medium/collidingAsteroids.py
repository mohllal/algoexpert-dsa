"""
O(n) time and O(n) space
n is the length of the input array
"""
def collidingAsteroids(asteroids):
    stack = []

    for asteroid in asteroids:
        if len(stack) == 0 or asteroid > 0:
            stack.append(asteroid)
            continue

        while len(stack) > 0 and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
            stack.pop()

        if len(stack) == 0 or stack[-1] < 0:
            stack.append(asteroid)
        elif abs(stack[-1]) == abs(asteroid):
            stack.pop()

    return stack