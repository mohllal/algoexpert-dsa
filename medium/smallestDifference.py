def smallestDifference(arrayOne, arrayTwo):
    return smallestDifferenceLogarithmicTimeAndConstantSpace(arrayOne, arrayTwo)


"""
O(n*m) time and O(1) space
n is the length of the first input array
m is the length of the second input array
"""
def smallestDifferenceQuadraticTimeAndConstantSpace(arrayOne, arrayTwo):
    result = [None] * 2
    smallest = float("inf")

    for i in range(0, len(arrayOne)):
        for j in range(0, len(arrayTwo)):
            difference = abs(arrayOne[i] - arrayTwo[j])
            if difference < smallest:
                smallest = difference
                result[0] = arrayOne[i]
                result[1] = arrayTwo[j]
    return result


"""
O(nlog(n)+mlog(m)) time and O(1) space
n is the length of the first input array
m is the length of the second input array
"""
def smallestDifferenceLogarithmicTimeAndConstantSpace(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    pointerOne = 0
    pointerTwo = 0
    smallest = float("inf")
    result = [None] * 2
    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        firstNumber = arrayOne[pointerOne]
        secondNumber = arrayTwo[pointerTwo]

        difference = abs(firstNumber - secondNumber)
        if difference == 0:
            return [firstNumber, secondNumber]

        if firstNumber < secondNumber:
            pointerOne += 1
        else:
            pointerTwo += 1

        if difference < smallest:
            smallest = difference
            result[0] = firstNumber
            result[1] = secondNumber

    return result