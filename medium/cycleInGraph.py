def cycleInGraph(edges):
    return cycleInGraphRecursive(edges)


"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def cycleInGraphRecursive(edges):
    graph = {i: edges[i] for i in range(len(edges))}
    visited = [False] * len(edges)
    recStack = [False] * len(edges)

    for vertex in graph:
        if not visited[vertex]:
            if isCyclic(graph, vertex, visited, recStack):
                return True

    return False

def isCyclic(graph, vertex, visited, recStack):
    visited[vertex] = True
    recStack[vertex] = True

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            if isCyclic(graph, neighbour, visited, recStack):
                return True
        elif recStack[neighbour]:
            return True

    recStack[vertex] = False
    return False


WHITE = 0
GREY = 1
BLACK = 2

"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def cycleInGraphAnotherRecursive(edges):
    graph = {i: edges[i] for i in range(len(edges))}
    colors = [WHITE] * len(edges)

    for vertex in graph:
        if colors[vertex] == WHITE:
            if isCyclicColored(graph, vertex, colors):
                return True
    return False

def isCyclicColored(graph, vertex, colors):
    colors[vertex] = GREY

    for neighbour in graph[vertex]:
        if colors[neighbour] == WHITE:
            if isCyclicColored(graph, neighbour, colors):
                return True
        elif colors[neighbour] == GREY:
            return True

    colors[vertex] = BLACK
    return False