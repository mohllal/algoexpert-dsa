import heapq

"""
O((v+e)log(v)) time and O(v) space
v is the number of vertices in the input graph
e is the number of edges in the input graph
"""
def dijkstrasAlgorithm(start, adjacency):
    distances = [float("inf") for _ in range(len(adjacency))]
    visited = [False for _ in range(len(adjacency))]
    parents = [-1 for _ in range(len(adjacency))]

    distances[start] = 0
    minHeap = [(0, start)]

    while len(minHeap) > 0:
        currDistance, currNode = heapq.heappop(minHeap) # O(log(v)) time
        visited[currNode] = True

        for destNode, destDistance in adjacency[currNode]:
            newDistance = currDistance + destDistance
            if newDistance < distances[destNode] and not visited[destNode]:
                distances[destNode] = newDistance
                parents[destNode] = currNode
                heapq.heappush(minHeap, (newDistance, destNode)) # O(log(v)) time

    return [distance if distance != float("inf") else -1 for distance in distances]