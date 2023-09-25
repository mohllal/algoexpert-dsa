def oneEdit(stringOne, stringTwo):
    return oneEditLinearTimeAndLinearSpace(stringOne, stringTwo)


"""
O(n) time and O(1) space
n is the length of the longest string
"""
def oneEditLinearTimeAndLinearSpace(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False

    edited = False
    startOne = 0
    startTwo = 0
    while startOne < len(stringOne) and startTwo < len(stringTwo):
        if stringOne[startOne] == stringTwo[startTwo]:
            startOne += 1
            startTwo += 1
        elif stringOne[startOne] != stringTwo[startTwo] and not edited:
            edited = True
            if len(stringOne) == len(stringTwo):
                startOne += 1
                startTwo += 1
            elif len(stringOne) > len(stringTwo):
                startOne += 1
            else:
                startTwo += 1
        elif stringOne[startOne] != stringTwo[startTwo] and edited:
            return False

    return True


"""
O(n) time and O(1) space
n is the length of the longest string
"""
def oneEditAnotherLinearTimeAndLinearSpace(stringOne, stringTwo):
    if abs(len(stringOne) - len(stringTwo)) > 1:
        return False

    if len(stringOne) == len(stringTwo):
        return replaceOp(stringOne, stringTwo)
    elif len(stringOne) > len(stringTwo):
        return removeOp(stringOne, stringTwo)
    elif len(stringTwo) > len(stringOne):
        return removeOp(stringTwo, stringOne)


def replaceOp(stringOne, stringTwo):
    edited = False
    startOne = 0

    while startOne < len(stringOne):
        if stringOne[startOne] != stringTwo[startOne] and not edited:
            edited = True
        elif stringOne[startOne] != stringTwo[startOne] and edited:
            return False
        startOne += 1

    return True

def removeOp(stringOne, stringTwo):
    edited = False
    startOne = 0
    startTwo = 0

    while startOne < len(stringOne) and startTwo < len(stringTwo):
        if stringOne[startOne] == stringTwo[startTwo]:
            startOne += 1
            startTwo += 1
        elif stringOne[startOne] != stringTwo[startTwo] and not edited:
            edited = True
            startOne += 1
        elif stringOne[startOne] != stringTwo[startTwo] and edited:
            return False

    return True
