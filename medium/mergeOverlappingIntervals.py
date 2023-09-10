"""
O(nlog(n)) time and O(n) space
n is the length of the input array
"""
def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda element: element[0])

    result = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] <= end:
            start = min(start, interval[0])
            end = max(end, interval[1])
        else:
            result.append([start, end])
            start = interval[0]
            end = interval[1]

    result.append([start, end])
    return result