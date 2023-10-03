def phoneNumberMnemonics(phoneNumber):
    return phoneNumberMnemonicsRecursive(phoneNumber)

"""
O(n*4^n) time and O(n*4^n) space
n is the number of the digits
"""
def phoneNumberMnemonicsRecursive(phoneNumber):
    def phoneNumberMnemonicsHelper(phoneNumber, associations, start, prefix, combinations):
        if start == len(phoneNumber):
            if len(prefix) != 0:
                combinations.append("".join(prefix[:]))
            return

        for button in associations[phoneNumber[start]]:
            prefix.append(button)
            phoneNumberMnemonicsHelper(phoneNumber, associations, start + 1, prefix, combinations)
            prefix.pop()

    associations = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    start = 0
    prefix = []
    combinations = []
    phoneNumberMnemonicsHelper(phoneNumber, associations, start, prefix, combinations)
    return combinations


"""
O(n*4^n) time and O(n*4^n) space
n is the number of the digits
"""
def phoneNumberMnemonicsIterative(phoneNumber):
    combinations = [""] if len(phoneNumber) > 0 else []
    associations = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    for digit in phoneNumber:
        current = []
        for button in associations[digit]:
            for combination in combinations:
                current.append(combination + button)
        combinations = current

    return combinations