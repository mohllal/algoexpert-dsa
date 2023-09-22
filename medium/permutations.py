def getPermutations(array):
    permutations = []
    getPermutationsThirdRecursive(array, 0, permutations)
    return permutations


"""
O(n^2*n!) time and O(n*n!) space
n is the length of the input array
"""
def getPermutationsRecursive(array):
    if len(array) == 1:
        return [array]

    permutations = []
    for i in range(0, len(array)):
        currentArray = array[:i] + array[i + 1:]
        currentPermutation = getPermutationsRecursive(currentArray)

        for j in range(0, len(currentPermutation)):
            permutations.append([array[i]] + currentPermutation[j])

    return permutations


"""
O(n^2*n!) time and O(n*n!) space
n is the length of the input array
"""
def getPermutationsSecondRecursive(array, currentPermutation, permutations):
    if len(array) == 0 and len(currentPermutation) != 0:
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutation + [array[i]]
            getPermutationsSecondRecursive(newArray, newPermutation, permutations)


"""
O(n*n!) time and O(n*n!) space
n is the length of the input array
"""
def getPermutationsThirdRecursive(array, index, permutations):
    if index == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(index, len(array)):
            array[index], array[j] = array[j], array[index]
            getPermutationsThirdRecursive(array, index + 1, permutations)
            array[index], array[j] = array[j], array[index]