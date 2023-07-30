def caesarCipherEncryptor(string, key):
    return caesarCipherEncryptorLinearTimeAndLinearSpace(string, key)


"""
O(n) time and O(n) space
n is the length of the input string
"""
def caesarCipherEncryptorLinearTimeAndLinearSpace(string, key):
    array = list(string)
    for i in range(0, len(array)):
        encrypted = (ord(array[i]) - ord('a') + key) % 26
        array[i] = chr(ord('a') + encrypted)

    return ''.join(array)


"""
O(n) time and O(n) space
n is the length of the input string
"""
def caesarCipherEncryptorAnotherLinearTimeAndLinearSpace(string, key):
    array = list(string)
    key %= 26

    for i in range(0, len(array)):
        encrypted = ord(array[i]) + key

        if encrypted <= 122:
            array[i] = chr(encrypted)
        else:
            encrypted %= 122
            array[i] = chr(ord('a') + encrypted - 1)
    return ''.join(array)