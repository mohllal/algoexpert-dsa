"""
O(n*log(n)) time and O(1) space
n is the length of the input array
"""
def sweetAndSavory(dishes, target):
    dishes.sort()

    pair = [0, 0]
    closest = float("inf")

    start = 0
    end = len(dishes) - 1
    while start < end:
        if dishes[start] > 0 or dishes[end] < 0:
            break

        diff = dishes[end] + dishes[start]
        if diff == target:
            return [dishes[start], dishes[end]]

        if diff < target:
            if target - diff < closest:
                closest = target - diff
                pair = [dishes[start], dishes[end]]
            start += 1
        else:
            end -= 1

    return pair