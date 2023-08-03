class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        return depthFirstSearchRecursive(self, array)


"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def depthFirstSearchRecursive(node, output, visited=None):
    if visited is None:
        visited = set()

    visited.add(node.name)
    output.append(node.name)

    for child in node.children:
        if child.name not in visited:
            depthFirstSearchRecursive(child, output, visited)

    return output


"""
O(v+e) time and O(v) space
v is the number of vertices of the input graph
e is the number of edges of the input graph
"""
def depthFirstSearchIterative(node, output):
    visited = set()
    stack = [node]

    while len(stack) > 0:
        current = stack.pop()
        visited.add(current.name)
        output.append(current.name)

        for i in reversed(range(len(current.children))):
            if current.children[i].name not in visited:
                stack.append(current.children[i])

    return output
