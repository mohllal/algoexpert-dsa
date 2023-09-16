"""
O(nlog(n)) time and O(n) space
n is the length of the input array
"""
def taskAssignment(k, tasks):
    sortedTasks = [[tasks[i], i] for i in range(0, len(tasks))]
    sortedTasks.sort(key=lambda x: x[0])

    current = 0
    pairs = [0] * k
    while current < k:
        firstTask = sortedTasks[current]
        secondTask = sortedTasks[len(tasks) - 1 - current]
        pairs[current] = [firstTask[1], secondTask[1]]

        current += 1

    return pairs