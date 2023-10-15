class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    return getYoungestCommonAncestorLinearTimeAndLinearSpace(topAncestor, descendantOne, descendantTwo)


"""
O(d) time and O(d) space
d is the depth of the ancestral tree
"""
def getYoungestCommonAncestorLinearTimeAndLinearSpace(topAncestor, descendantOne, descendantTwo):
    visited = set()

    firstYoungestCommonAncestor = traverseAncestralTree(descendantOne, visited)
    secondYoungestCommonAncestor = traverseAncestralTree(descendantTwo, visited)

    return firstYoungestCommonAncestor if firstYoungestCommonAncestor is not None else secondYoungestCommonAncestor


def traverseAncestralTree(tree, visited):
    current = tree

    while current is not None:
        if current.name not in visited:
            visited.add(current.name)
        else:
            return current

        current = current.ancestor

"""
O(d) time and O(1) space
d is the depth of the ancestral tree
"""
def getYoungestCommonAncestorLinearTimeAndConstantSpace(topAncestor, descendantOne, descendantTwo):
    descendantOneDepth = getAncestralTreeDepth(descendantOne)
    descendantTwoDepth = getAncestralTreeDepth(descendantTwo)

    descendantOne = cutAncestralTreeDepth(descendantOne, descendantOneDepth - descendantTwoDepth)
    descendantTwo = cutAncestralTreeDepth(descendantTwo, descendantTwoDepth - descendantOneDepth)

    currentDescendantOne = descendantOne
    currentDescendantTwo = descendantTwo

    while currentDescendantOne != currentDescendantTwo:
        currentDescendantOne = currentDescendantOne.ancestor
        currentDescendantTwo = currentDescendantTwo.ancestor

    return currentDescendantOne


def getAncestralTreeDepth(tree):
    depth = 0
    current = tree

    while current is not None:
        current = current.ancestor
        depth += 1

    return depth

def cutAncestralTreeDepth(tree, depth):
    current = tree

    while depth > 0:
        current = current.ancestor
        depth -= 1

    return current
