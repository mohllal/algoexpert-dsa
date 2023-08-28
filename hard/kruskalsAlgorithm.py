"""
O(elog(e)) time and O(e+v) space
e is the number of edges in the input graph
v is the number of vertices in the input graph
"""
def kruskalsAlgorithm(adjacency):
    n = len(adjacency)
    parent, rank = createSet(n)

    edges = []
    for i in range(n):
        for j in range(len(adjacency[i])):
            if adjacency[i][j][0] > i:
                edges.append([i, adjacency[i][j][0], adjacency[i][j][1]])

    edges.sort(key=lambda edge: edge[2])

    result = [[] for _ in range(n)]
    for edge in edges:
        if find(parent, edge[0]) != find(parent, edge[1]):
            result[edge[0]].append([edge[1], edge[2]])
            result[edge[1]].append([edge[0], edge[2]])
            union(parent, rank, edge[0], edge[1])

    return result


"""
O(v) time and O(v) space
v is the number of vertices in the input graph
"""
def createSet(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank


"""
O(α(v)) time and O(α(v)) space
O(1) time amortized and O(1) space amortized
v is the number of vertices in the input graph
"""
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


"""
O(α(v)) time and O(α(v)) space
O(1) time amortized and O(1) space amortized
v is the number of vertices in the input graph
"""
def union(parent, rank, x, y):
    parentX = find(parent, x)
    parentY = find(parent, y)

    if parentX == parentY:
        return False

    if rank[parentX] < rank[parentY]:
        parent[parentX] = parentY
    elif rank[parentY] < rank[parentX]:
        parent[parentY] = parentX
    else:
        parent[parentX] = parentY
        rank[parentY] += 1
    return True