def threeNumberSum(array, targetSum):
    return threeNumberSumAnotherQuadraticTimeAndLinearSpace(array, targetSum)


"""
O(n^3) time and O(n) space
n is the length of the input array
"""
def threeNumberSumCubicTimeAndLinearSpace(array, target):
    array.sort()

    result = []
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == target:
                    result.append([array[i], array[j], array[k]])
    return result


"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def threeNumberSumQuadraticTimeAndLinearSpace(array, target):
    exists = {element: True for element in array}

    triplets = set()
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            diff = target - (array[i] + array[j])

            if diff in exists and diff != array[i] and diff != array[j]:
                minimum = min(array[i], array[j], diff)
                maximum = max(array[i], array[j], diff)
                middle = target - (minimum + maximum)

                triplets.add((minimum, middle, maximum))

    result = list(triplets)
    result.sort(key=lambda elem: (elem[0], elem[1], elem[2]))
    return result


"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def threeNumberSumAnotherQuadraticTimeAndLinearSpace(array, target):
    array.sort()

    result = []
    for i in range(0, len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while right > left:
            current = array[i] + array[left] + array[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
    return result