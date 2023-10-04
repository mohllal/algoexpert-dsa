import functools

def hasSingleCycle(array):
    return hasSingleCycleLinearTimeAndLinearSpace(array)


"""
O(n) time and O(n) space
n is the length of the input array
"""
def hasSingleCycleLinearTimeAndLinearSpace(array):
    graph = {}
    visited = [False] * len(array)
    visits = [0] * len(array)
    recStack = [False] * len(array)

    for i in range(len(array)):
        neighbour = i + array[i]
        graph[i] = [neighbour % len(array)]

    hasCycle = isCyclic(graph, 0, visited, visits, recStack)
    allVerticesAreVisited = functools.reduce(lambda a, b: a and b, visited)
    allVerticesAreVisitedOnce = functools.reduce(lambda a, b: a * b, visits[1:])

    return hasCycle and allVerticesAreVisited and allVerticesAreVisitedOnce == 1

def isCyclic(graph, vertex, visited, visits, recStack):
    visited[vertex] = True
    recStack[vertex] = True
    visits[vertex] += 1

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            if isCyclic(graph, neighbour, visited, visits, recStack):
                return True
        elif recStack[neighbour]:
            visits[neighbour] += 1
            return True

    recStack[vertex] = False
    return False


"""
O(n) time and O(1) space
n is the length of the input array
"""
def hasSingleCycleLinearTimeAndConstantSpace(array):
    jumps = 0
    current = 0

    while jumps < len(array):
        if jumps > 0 and current == 0:
            return False

        current = (current + array[current]) % len(array)
        jumps += 1

    return current == 0