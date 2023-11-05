def fourNumberSum(array, targetSum):
    return fourNumberSumCubicTimeAndQuadraticSpace(array, targetSum)

"""
O(n^3) time and O(n^2) space
n is the length of the input array
"""
def fourNumberSumCubicTimeAndQuadraticSpace(array, targetSum):
    result = []
    presence = {num: True for num in array}
    visited = set()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                current = array[i] + array[j] + array[k]
                remaining = targetSum - current

                if (
                    remaining in presence and
                    remaining != array[i] and
                    remaining != array[j] and
                    remaining != array[k]
                ):
                    quadruplet = [array[i], array[j], array[k], remaining]
                    quadruplet.sort()
                    quadruplet = tuple(quadruplet)

                    if quadruplet not in visited:
                        visited.add(quadruplet)
                        result.append([array[i], array[j], array[k], remaining])

    return result


"""
O(n^2) time and O(n^2) space
n is the length of the input array
"""
def fourNumberSumQuadraticTimeAndQuadraticSpace(array, targetSum):
    result = []
    pairsSum = {}
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            current = array[i] + array[j]
            if current not in pairsSum:
                pairsSum[current] = []
            pairsSum[current].append([array[i], array[j]])

    visited = set()
    for fSum, fPair in pairsSum.items():
        for sSum, sPair in pairsSum.items():
            if fSum == sSum or fSum + sSum != targetSum:
                continue

            quadruplets = []
            for i in range(len(fPair)):
                for j in range(len(sPair)):
                    quadruplet = fPair[i] + sPair[j]
                    quadruplet.sort()
                    quadruplet = tuple(quadruplet)

                    if quadruplet not in visited and len(set(quadruplet)) == 4:
                        visited.add(quadruplet)
                        quadruplets.append(fPair[i] + sPair[j])

            result.extend(quadruplets)

    return result

"""
O(n^2) time and O(n^2) space
n is the length of the input array
"""
def fourNumberSumAnotherQuadraticTimeAndQuadraticSpace(array, targetSum):
    result = []
    pairSums = {}
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            current = array[i] + array[j]
            remaining = targetSum - current

            if remaining in pairSums:
                for pair in pairSums[remaining]:
                    result.append(pair + [array[i], array[j]])

        for k in range(i):
            current = array[i] + array[k]
            if current not in pairSums:
                pairSums[current] = []
            pairSums[current].append([array[i], array[k]])

    return result
