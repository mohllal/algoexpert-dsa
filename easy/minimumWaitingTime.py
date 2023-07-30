"""
O(nlog(n)) time and O(1) space
n is the length of the input array
"""
def minimumWaitingTime(queries):
    queries.sort()

    minimumWaitingTime = 0
    currentWaitingTime = 0
    for i in range(1, len(queries)):
        minimumWaitingTime += currentWaitingTime + queries[i - 1]
        currentWaitingTime += queries[i - 1]

    return minimumWaitingTime