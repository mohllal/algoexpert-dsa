from math import ceil
from collections import deque

"""
O(n*m) time and O(n*m) space
n is the horizontal distance between the input knights
m is the vertical distance between the input knights
"""
def knightConnection(knightA, knightB):
    moves = -1
    visited = set()

    queue = deque([[knightA[0], knightA[1], 0]])
    while len(queue):
        current = queue.popleft()

        if current[0] == knightB[0] and current[1] == knightB[1]:
            return ceil(current[2] / 2)

        turns = getTurns(current)
        for turn in turns:
            if turn not in visited:
                queue.append([turn[0], turn[1], current[2] + 1])
                visited.add(turn)

    return moves

def getTurns(knight):
    turns = [
        [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]
    ]

    return [
        (knight[0] + turn[0], knight[1] + turn[1])
        for turn in turns
    ]