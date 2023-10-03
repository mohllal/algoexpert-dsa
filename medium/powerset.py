def powerset(array):
    return powersetRecursive(array)


"""
O(n*2^n) time and O(n*2^n) space
n is the length of the input array
"""
def powersetRecursive(array):
    def powersetHelper(array, prefix, start, powerset):
        powerset.append(prefix[:])

        for i in range(start, len(array)):
            prefix.append(array[i])
            powersetHelper(array, prefix, i + 1, powerset)
            prefix.pop()

    prefix = []
    powerset = []
    start = 0
    powersetHelper(array, prefix, start, powerset)
    return powerset


"""
O(n*2^n) time and O(n*2^n) space
n is the length of the input array
"""
def powersetIterative(array):
    powerset = [[]]

    for i in range(len(array)):
        for j in range(len(powerset)):
            current = powerset[j] + [array[i]]
            powerset.append(current)

    return powerset