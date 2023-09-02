def arrayOfProducts(array):
    return arrayOfProductsQuadraticTimeAndLinearSpace(array)


"""
O(n^2) time and O(n) space
n is the length of the input array
"""
def arrayOfProductsQuadraticTimeAndLinearSpace(array):
    products = []
    for i in range(0, len(array)):
        product = 1
        for j in range(0, len(array)):
            if i != j:
                product *= array[j]
        products.append(product)
    return products


"""
O(n) time and O(n) space
n is the length of the input array
"""
def arrayOfProductsLinearTimeAndLinearSpace(array):
    left = 1
    right = 1
    for i in range(1, len(array)):
        right *= array[i]

    products = [left * right]
    for i in range(1, len(array)):
        left *= array[i - 1]
        right = divide(right, array[i])
        products.append(left * right)

    return products

"""
O(1) time and O(1) space
"""
def divide(a, b):
    if a == 0:
        return 0

    aNegative = a < 0
    bNegative = b < 0

    answer = 0
    a = abs(a)
    b = abs(b)

    for i in range(31, -1, -1):
        if b << i <= a:
            a -= (b << i)
            answer += (1 << i)

    if aNegative:
        answer *= -1
    if bNegative:
        answer *= -1

    return answer


"""
O(n) time and O(n) space
n is the length of the input array
"""
def arrayOfProductsAnotherLinearTimeAndLinearSpace(array):
    leftProducts = [1 for _ in range(0, len(array))]
    rightProducts = [1 for _ in range(0, len(array))]

    currentLeftProduct = 1
    for i in range(0, len(array)):
        leftProducts[i] = currentLeftProduct
        currentLeftProduct *= array[i]

    currentRightProduct = 1
    for i in reversed(range(0, len(array))):
        rightProducts[i] = currentRightProduct
        currentRightProduct *= array[i]

    products = [leftProducts[i] * rightProducts[i] for i in range(0, len(array))]
    return products
