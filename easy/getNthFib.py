def getNthFib(n):
    return getNthFibLinearTimeAndConstantSpace(n)


"""
O(n) time and O(1) space
n is the input number
"""
def getNthFibLinearTimeAndConstantSpace(n):
    f = [0, 1]
    for _ in range(3, n + 1):
        current = f[0] + f[1]
        f[0] = f[1]
        f[1] = current

    return f[1] if n > 1 else f[0]


"""
O(2^n) time and O(n) space
n is the input number
"""
def getNthFibRecursiveExponentialTimeAndLinearSpace(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (
            getNthFibRecursiveExponentialTimeAndLinearSpace(n - 1)
            + getNthFibRecursiveExponentialTimeAndLinearSpace(n - 2)
        )
