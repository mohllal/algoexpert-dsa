def quickSort(array):
    return quickSortLogLinearTimeAndLinearSpace(array)

"""
average: O(nlog(n)) time and O(n) space
worst: O(n^2) time and O(n) space
n is the length of the input array
"""
def quickSortLogLinearTimeAndLinearSpace(array):
    def quickSortHelper(array):
        if len(array) < 2:
            return array

        pivot = array[0]

        left = [x for x in array[1:] if x <= pivot]
        right = [x for x in array[1:] if x > pivot]
        return quickSortHelper(left) + [pivot] + quickSortHelper(right)

    return quickSortHelper(array)


"""
average: O(nlog(n)) time and O(log(n)) space
worst: O(n^2) time and O(log(n)) space
n is the length of the input array
"""
def quickSortLogLinearTimeAndLogLinearSpace(array):
    def quickSortHelper(array, start, end):
        if end <= start:
            return array

        pivot = partition(array, start, end)

        quickSortHelper(array, start, pivot - 1)
        quickSortHelper(array, pivot + 1, end)
        return array


    def partition(array, start, end):
        pivot = array[end]

        i = start - 1
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1

    return quickSortHelper(array, 0, len(array) - 1)