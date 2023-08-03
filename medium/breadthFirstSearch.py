import collections

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        return breadthFirstSearchIterative(self, array)


"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def breadthFirstSearchIterative(node, output):
    visited = set()
    queue = collections.deque([node])

    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current.name)
        output.append(current.name)

        for child in current.children:
            if child.name not in visited:
                queue.append(child)

    return output


"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def breadthFirstSearchRecursive(queue, output, visited=None):
    if visited is None:
        visited = set()

    if len(queue) == 0:
        return

    current = queue.popleft()
    visited.add(current.name)
    output.append(current.name)

    for child in current.children:
        if child.name not in visited:
            queue.append(child)

    breadthFirstSearchRecursive(queue, output, visited)
    return output
