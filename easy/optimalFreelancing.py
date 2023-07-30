"""
O(n) time and O(1) space
n is the length of the input array
"""
def optimalFreelancing(jobs):
    profit = 0
    currentDay = 7
    while currentDay > 0 and len(jobs) > 0:
        currentDayMaxPayment = 0
        currentDayJobIndex = None
        for index, job in enumerate(jobs):
            if job["deadline"] >= currentDay:
                if job["payment"] > currentDayMaxPayment:
                    currentDayMaxPayment = job["payment"]
                    currentDayJobIndex = index

        if currentDayJobIndex is not None:
            jobs.pop(currentDayJobIndex)
            profit += currentDayMaxPayment

        currentDay -= 1

    return profit
