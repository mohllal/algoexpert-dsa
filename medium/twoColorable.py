"""
O(v+e) time and O(v) space
v is the number of vertices in the graph
e is the number of edges in the graph
"""
def twoColorable(edges):
    graph = {i: edges[i] for i in range(len(edges))}

    visited = [False] * len(edges)
    colors = [-1] * len(edges)
    colors[0] = 1

    return isBipartite(graph, 0, visited, colors)


def isBipartite(graph, node, visited, colors):
    visited[node] = True

    for neighbour in graph[node]:
        if not visited[neighbour]:
            colors[neighbour] = 1 if colors[node] == 0 else 0

            if not isBipartite(graph, neighbour, visited, colors):
                return False

        elif colors[neighbour] == colors[node]:
            return False
    return True