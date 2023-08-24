
def sunsetViews(buildings, direction):
    return sunsetViewsLinearTimeAndLinearSpace(buildings, direction)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def sunsetViewsLinearTimeAndLinearSpace(buildings, direction):
    longest = float("-inf")

    ranges = range(0, len(buildings))
    if direction == "EAST":
        ranges = reversed(ranges)

    result = []
    for i in ranges:
        if buildings[i] > longest:
            result.append(i)
            longest = buildings[i]

    if direction == "EAST":
        result = list(reversed(result))
    return result


"""
O(n) time and O(n) space
n is the length of the input array
"""
def sunsetViewsAnotherLinearTimeAndLinearSpace(buildings, direction):
    result = []

    ranges = range(0, len(buildings))
    if direction == "WEST":
        ranges = reversed(ranges)

    for i in ranges:
        while len(result) > 0 and buildings[result[-1]] <= buildings[i]:
            result.pop()
        result.append(i)

    if direction == "WEST":
        result = list(reversed(result))

    return result

