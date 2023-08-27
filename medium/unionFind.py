class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    """
    O(1) time and O(1) space
    n is the number of elements
    """
    def createSet(self, value):
        self.parent[value] = value
        self.rank[value] = 0


    """
    O(α(n)) time and O(α(n)) space
    O(1) time amortized and O(1) space amortized
    n is the number of elements
    """
    def find(self, x):
        if x not in self.parent:
            return None

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    """
    O(α(n)) time and O(α(n)) space
    O(1) time amortized and O(1) space amortized
    n is the number of elements
    """
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX is None or parentY is None or parentX == parentY:
            return

        if self.rank[parentX] < self.rank[parentY]:
            self.parent[parentX] = parentY
        elif self.rank[parentY] < self.rank[parentX]:
            self.parent[parentY] = parentX
        else:
            self.parent[parentX] = parentY
            self.rank[parentY] += 1
