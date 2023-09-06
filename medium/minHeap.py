class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    """
    O(n) time and O(1) space - amortized complexity
    n is the length of the input array
    """
    def buildHeap(self, array):
        n = len(array)

        for i in range(n // 2, -1, -1):
            self.siftDownRecursive(i, array)

        return array

    """
    O(log(n)) time and O(log(n)) space
    n is the length of the input array
    """
    def siftDownRecursive(self, i, heap):
        n = len(heap)
        smallest = i

        left = (2 * i) + 1
        if left < n and heap[left] < heap[smallest]:
            smallest = left

        right = (2 * i) + 2
        if right < n and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.siftDownRecursive(smallest, heap)

    """
    O(log(n)) time and O(1) space
    n is the length of the input array
    """
    def siftDownIterative(self, i, heap):
        n = len(heap)
        while True:
            smallest = i

            left = (2 * i) + 1
            if left < n and heap[left] < heap[smallest]:
                smallest = left

            right = (2 * i) + 2
            if right < n and heap[right] < heap[smallest]:
                smallest = right

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest

    """
    O(log(n)) time and O(log(n)) space
    n is the length of the input array
    """
    def siftUpRecursive(self, i, heap):
        if i == 0:
            return

        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            self.siftUpRecursive(parent, heap)

    """
    O(log(n)) time and O(1) space
    n is the length of the input array
    """
    def siftUpIterative(self, i, heap):
        parent = (i - 1) // 2
        while i > 0 and heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
            parent = (i - 1) // 2

    """
    O(log(n)) time and O(log(n)) space
    n is the length of the input array
    """
    def remove(self):
        minimum = self.heap[0]

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.siftDownRecursive(0, self.heap)
        return minimum

    """
    O(log(n)) time and O(log(n)) space
    n is the length of the input array
    """
    def insert(self, value):
        self.heap.append(value)
        n = len(self.heap)
        self.siftUpRecursive(n - 1, self.heap)

    """
    O(1) time and O(1) space
    """
    def peek(self):
        return self.heap[0]


