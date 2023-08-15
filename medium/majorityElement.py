
def majorityElement(array):
    return majorityElementLinearTimeAndConstantSpace(array)


"""
O(n) time and O(1) space
n is the lenght of the input array
"""
def majorityElementLinearTimeAndConstantSpace(array):
    candidate, count = array[0], 1

    for i in range(1, len(array)):
        if count == 0:
            candidate = array[i]

        if candidate == array[i]:
            count += 1
        else:
            count -= 1

    return candidate


"""
O(n) time and O(1) space
n is the lenght of the input array
"""
def majorityElementAnotherLinearTimeAndConstantSpace(array):
    majority = 0

    for bit in range(0, 32):
        bitValue = 1 << bit

        count = 0
        for number in array:
            if (number & bitValue) != 0:
                count += 1

        if count > len(array) // 2:
            majority += bitValue

    return majority